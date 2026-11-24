"""Implementation of the public API. Keep this module free of I/O."""

import re

_NON_ALPHANUMERIC = re.compile(r"[^a-z0-9]+")


def slugify(text: str, *, separator: str = "-") -> str:
    """Return a URL-friendly slug of ``text``.

    The text is lowercased, and each run of characters other than ASCII letters and digits
    becomes one ``separator``. Raise ``ValueError`` when nothing is left, rather than
    returning an empty slug.
    """
    parts = [part for part in _NON_ALPHANUMERIC.split(text.lower()) if part]
    if not parts:
        raise ValueError("text has no ASCII letters or digits to slugify")
    return separator.join(parts)
