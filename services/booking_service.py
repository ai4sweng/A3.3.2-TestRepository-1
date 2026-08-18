"""
Business logic related to creating and managing bookings.

Orchestrates the repositories (database) and applies the business
rules, without knowing details of how the HTTP routes are exposed (api).
"""

from core.config import get_settings
from core.exceptions import (
    BookingLimitExceededError,
    BookingNotFoundError,
    InvalidBookingDatesError,
)
from database.models import Booking, BookingStatus
from database.repositories.booking_repository import BookingRepository
from database.repositories.user_repository import UserRepository
from database.session import get_db
from services.pricing_service import calculate_total_price
from utils.date_helpers import is_valid_date_range


class BookingService:
    """Use cases related to bookings."""

    def __init__(self):
        self.booking_repo = BookingRepository()
        self.user_repo = UserRepository()
        self.settings = get_settings()

    def create_booking(
        self,
        user_id: int,
        destination_id: int,
        check_in,
        check_out,
        passengers: int = 1,
    ) -> Booking:
        """Creates a new booking for a user, validating business rules."""
        if not is_valid_date_range(check_in, check_out):
            raise InvalidBookingDatesError("Invalid date range")

        existing = self.booking_repo.list_by_user(user_id)
        active = [b for b in existing if b.status != BookingStatus.CANCELLED]
        if len(active) >= self.settings.max_bookings_per_user:
            raise BookingLimitExceededError(
                f"User {user_id} already has the maximum number of active bookings"
            )

        destination = get_db().destinations[destination_id]
        total_price = calculate_total_price(
            destination, check_in, check_out, passengers
        )

        booking = Booking(
            id=0,
            user_id=user_id,
            destination_id=destination_id,
            check_in=check_in,
            check_out=check_out,
            status=BookingStatus.PENDING,
            total_price=total_price,
            passengers=passengers,
        )
        return self.booking_repo.add(booking)

    def cancel_booking(self, booking_id: int) -> Booking:
        """Cancels an existing booking."""
        booking = self.booking_repo.get_by_id(booking_id)
        if booking is None:
            raise BookingNotFoundError(f"Booking {booking_id} not found")
        booking.status = BookingStatus.CANCELLED
        return self.booking_repo.update(booking)

    def get_user_bookings(self, user_id: int) -> list[Booking]:
        """Returns all bookings for a user."""
        return self.booking_repo.list_by_user(user_id)
