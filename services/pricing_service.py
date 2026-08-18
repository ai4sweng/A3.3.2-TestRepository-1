"""
Business logic related to price calculation.
"""

from datetime import date

from database.models import Destination


def calculate_nights(check_in: date, check_out: date) -> int:
    """Calculates the number of nights between two dates."""
    return (check_out - check_in).days


def calculate_total_price(
    destination: Destination, check_in: date, check_out: date, passengers: int
) -> float:
    """Calculates the total price of a booking.

    Applies the destination's base price per night, per passenger, and
    a discount for long stays.
    """
    nights = calculate_nights(check_in, check_out)
    if nights <= 0:
        raise ValueError("check_out must be later than check_in")

    subtotal = destination.base_price * nights * passengers
    return apply_long_stay_discount(subtotal, nights)


def apply_long_stay_discount(subtotal: float, nights: int) -> float:
    """Applies a 10% discount if the stay is 7 nights or more."""
    if nights >= 7:
        return round(subtotal * 0.9, 2)
    return round(subtotal, 2)
