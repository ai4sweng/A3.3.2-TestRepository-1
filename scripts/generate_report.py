"""
Maintenance script: generates a text report of the system's confirmed
bookings.

This is a standalone administrative tool, meant to be run manually
(e.g. from a cron job).

Usage:
    python scripts/generate_report.py
"""

from database.models import BookingStatus
from database.session import get_db


def generate_confirmed_bookings_report() -> str:
    db = get_db()
    confirmed = [b for b in db.bookings.values() if b.status == BookingStatus.CONFIRMED]

    lines = [f"Confirmed bookings report ({len(confirmed)})", "-" * 40]
    for booking in confirmed:
        destination = db.destinations[booking.destination_id]
        lines.append(
            f"Booking #{booking.id} - {destination.city} - {booking.total_price} EUR"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    print(generate_confirmed_bookings_report())
