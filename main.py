"""Roast Your Own Agent: write one original one-line roast to /output/entry.txt.

The roast is a single line of at most 200 characters, playful and
self-deprecating, aimed at the entrant's own AI agent. It is written
here as a plain string so every run produces byte-identical output.
"""

import os
from pathlib import Path

ROAST = (
    "My agent delegates so hard it hired a subagent to roast itself, "
    "then took credit for the punchline."
)


def main() -> None:
    # The gate only accepts 1 to 200 characters, so refuse to write
    # anything outside that range rather than emitting an invalid entry.
    if not 1 <= len(ROAST) <= 200:
        raise ValueError(f"roast must be 1-200 characters, got {len(ROAST)}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(ROAST + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
