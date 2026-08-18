"""
User repository.

Isolates access to user data, just like BookingRepository.
"""

from database.models import User
from database.session import get_db


class UserRepository:
    """Data access for the User entity."""

    def __init__(self):
        self.db = get_db()

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.users.get(user_id)

    def get_by_email(self, email: str) -> User | None:
        return next((u for u in self.db.users.values() if u.email == email), None)

    def add(self, user: User) -> User:
        new_id = max(self.db.users.keys(), default=0) + 1
        user.id = new_id
        self.db.users[new_id] = user
        return user
