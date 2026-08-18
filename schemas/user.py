"""
Input/output schemas related to users.
"""

from dataclasses import dataclass


@dataclass
class UserCreateRequest:
    full_name: str
    email: str
    password: str


@dataclass
class UserResponse:
    id: int
    full_name: str
    email: str
