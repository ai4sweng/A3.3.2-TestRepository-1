"""Unit tests for utils/validators.py"""

from utils.validators import is_positive_integer, is_valid_email


def test_valid_email():
    assert is_valid_email("ana@example.com") is True


def test_invalid_email():
    assert is_valid_email("not-an-email") is False


def test_positive_integer():
    assert is_positive_integer(5) is True
    assert is_positive_integer(-1) is False
    assert is_positive_integer("5") is False
