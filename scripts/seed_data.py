"""
Maintenance script: seeds the database with sample data.

Usage:
    python scripts/seed_data.py
"""

from database.models import Destination
from database.session import get_db


def seed_extra_destinations():
    db = get_db()
    extra = [
        Destination(4, "Marrakech", "Morocco", 340.0),
        Destination(5, "Reykjavik", "Iceland", 780.0),
    ]
    for destination in extra:
        db.destinations[destination.id] = destination
    print(f"Inserted {len(extra)} additional destinations.")


if __name__ == "__main__":
    seed_extra_destinations()
