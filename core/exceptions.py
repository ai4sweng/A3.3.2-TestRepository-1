"""
Domain-specific exceptions for TravelHub.

Used across the different layers to signal business errors, instead of
letting generic Python exceptions propagate.
"""


class TravelHubError(Exception):
    """Base exception for all application-specific errors."""


class BookingNotFoundError(TravelHubError):
    """Raised when a requested booking cannot be found."""


class InvalidBookingDatesError(TravelHubError):
    """Raised when a booking's dates are not valid."""


class UserNotFoundError(TravelHubError):
    """Raised when a requested user cannot be found."""


class BookingLimitExceededError(TravelHubError):
    """Raised when a user exceeds the maximum number of active bookings."""
