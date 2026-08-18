"""
Helper functions for working with dates.

"""

from datetime import date, timedelta


def is_valid_date_range(check_in: date, check_out: date) -> bool:
    """Checks that check_out is later than check_in and not in the past."""
    if check_out <= check_in:
        return False
    if check_in < date.today():
        return False
    return True


def days_between(start: date, end: date) -> int:
    """Returns the number of days between two dates."""
    return (end - start).days


def add_days(base_date: date, days: int) -> date:
    """Adds a number of days to a given date."""
    return base_date + timedelta(days=days)
