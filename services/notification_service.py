"""
User notification service.

"""

from database.models import Booking, User


def notify_booking_confirmed(user: User, booking: Booking) -> str:
    """Generates (and "sends") the confirmation message for a booking."""
    message = (
        f"Hello {user.full_name}, your booking #{booking.id} has been confirmed. "
        f"Total: {booking.total_price} EUR."
    )
    print(f"[notification] -> {user.email}: {message}")
    return message


def notify_booking_cancelled(user: User, booking: Booking) -> str:
    """Generates (and "sends") the cancellation message for a booking."""
    message = f"Hello {user.full_name}, your booking #{booking.id} has been cancelled."
    print(f"[notification] -> {user.email}: {message}")
    return message
