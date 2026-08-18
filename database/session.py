"""
Database connection/session management.

Simulated with in-memory structures instead of a real database, but it
keeps the interface a real SQLAlchemy session would have, so the rest
of the layers won't need to change if a real database is connected
later on.
"""

from datetime import date

from database.models import Booking, BookingStatus, Destination, User


class InMemoryDatabase:
    """Simulates the application's persistent storage."""

    def __init__(self):
        self.users = {
            1: User(1, "Ana Torres", "ana@example.com", "hash1"),
            2: User(2, "Luis Marín", "luis@example.com", "hash2"),
        }
        self.destinations = {
            1: Destination(1, "Lisbon", "Portugal", 180.0),
            2: Destination(2, "Kyoto", "Japan", 950.0),
            3: Destination(3, "Cusco", "Peru", 620.0),
        }
        self.bookings = {
            1: Booking(
                1,
                1,
                1,
                date(2026, 3, 10),
                date(2026, 3, 15),
                BookingStatus.CONFIRMED,
                900.0,
                2,
            ),
        }
        self._next_booking_id = 2


_db = InMemoryDatabase()


def get_db() -> InMemoryDatabase:
    """Returns the application's (simulated) database instance."""
    return _db
