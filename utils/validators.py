"""
Generic input data validators.
"""

import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(email: str) -> bool:
    """Checks whether a string has a valid email format."""
    return bool(EMAIL_REGEX.match(email))


def is_positive_integer(value) -> bool:
    """Checks whether a value is a positive integer."""
    return isinstance(value, int) and value > 0
