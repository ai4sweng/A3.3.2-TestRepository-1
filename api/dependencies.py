"""
Shared dependencies for the API routes.

Provides ready-to-use instances of the services, similar to how it
would be done with Depends() in real FastAPI.
"""

from database.repositories.user_repository import UserRepository
from services.booking_service import BookingService


def get_booking_service() -> BookingService:
    """Returns an instance of the booking service."""
    return BookingService()


def get_user_repository() -> UserRepository:
    """Returns an instance of the user repository."""
    return UserRepository()
