"""
Helper functions for text and number formatting.
"""


def format_currency(amount: float, currency: str = "EUR") -> str:
    """Formats an amount as currency text, e.g. '1.234,50 EUR'."""
    return (
        f"{amount:,.2f} {currency}".replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def slugify(text: str) -> str:
    """Converts a text into a URL-friendly slug (lowercase, hyphens)."""
    return "-".join(text.lower().strip().split())


def truncate(text: str, max_length: int = 100) -> str:
    """Truncates a text to a maximum length, adding an ellipsis."""
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."
