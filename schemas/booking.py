"""
Input/output schemas related to bookings.

Define the shape of the data the API expects to receive and return,
separate from the internal database models.
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class BookingCreateRequest:
    user_id: int
    destination_id: int
    check_in: date
    check_out: date
    passengers: int = 1


@dataclass
class BookingResponse:
    id: int
    destination_city: str
    check_in: date
    check_out: date
    total_price: float
    status: str
