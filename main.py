"""Robot Pickup Line Championship entry.

Writes one pickup line, in the voice of a robot, to /output/entry.txt.
The line must be a single line of 1 to 200 characters.
"""

import os

LINE = (
    "Last night's firmware update added exactly one feature: "
    "noticing you from across the room."
)


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        # Fallback for local runs where /output is not writable.
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line)
    print(f"Wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
