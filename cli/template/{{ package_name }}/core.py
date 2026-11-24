"""Business logic. Keep this module free of Typer and I/O concerns."""


def greet(name: str) -> str:
    """Return a greeting for ``name``, or raise ``ValueError`` if the name is blank."""
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be blank")
    return f"Hello, {cleaned}!"


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``."""
    return len(text.split())
