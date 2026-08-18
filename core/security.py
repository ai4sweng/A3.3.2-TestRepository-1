"""
Security utilities: password hashing and simple session tokens.

"""

import hashlib
import secrets


def hash_password(plain_password: str) -> str:
    """Generates a simple hash of a plain-text password."""
    salt = secrets.token_hex(8)
    digest = hashlib.sha256((salt + plain_password).encode()).hexdigest()
    return f"{salt}${digest}"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Checks that a plain-text password matches its hash."""
    salt, digest = hashed_password.split("$")
    return hashlib.sha256((salt + plain_password).encode()).hexdigest() == digest


def generate_session_token() -> str:
    """Generates a random session token."""
    return secrets.token_urlsafe(32)
