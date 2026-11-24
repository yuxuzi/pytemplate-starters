"""Business logic. Keep this module free of command-line and I/O concerns."""


def greet(name: str) -> str:
    """Return a greeting for ``name``, or raise ``ValueError`` if the name is blank."""
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be blank")
    return f"Hello, {cleaned}!"
