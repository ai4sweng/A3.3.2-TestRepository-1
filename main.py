"""
Entry point of the TravelHub application.

Starts the API and registers the available routes.
"""

from api.routes import bookings, destinations, users
from core.config import get_settings


def create_app():
    """Creates and configures the application (simulated, no real framework)."""
    settings = get_settings()
    routes = {
        "bookings": bookings.router,
        "destinations": destinations.router,
        "users": users.router,
    }
    print(f"Starting {settings.app_name} in {settings.environment} mode")
    print(f"Registered route groups: {list(routes.keys())}")
    return routes


if __name__ == "__main__":
    create_app()
