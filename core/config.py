"""
Global application configuration.

Centralizes the parameters that depend on the environment (dev, staging, prod).
"""

import os
from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "TravelHub"
    environment: str = os.getenv("ENVIRONMENT", "development")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///travelhub.db")
    max_bookings_per_user: int = 5


_settings = Settings()


def get_settings() -> Settings:
    """Returns the application configuration (simple singleton)."""
    return _settings
