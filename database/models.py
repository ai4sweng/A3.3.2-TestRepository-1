"""
TravelHub data models.

Represent the domain entities as they are stored in the database. There
is no business logic here, only the shape of the data.
"""

from dataclasses import dataclass
from datetime import date
from enum import Enum


class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


@dataclass
class User:
    id: int
    full_name: str
    email: str
    hashed_password: str
    is_active: bool = True


@dataclass
class Destination:
    id: int
    city: str
    country: str
    base_price: float


@dataclass
class Booking:
    id: int
    user_id: int
    destination_id: int
    check_in: date
    check_out: date
    status: BookingStatus = BookingStatus.PENDING
    total_price: float = 0.0
    passengers: int = 1
