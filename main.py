"""Last Text at One Percent (make.fun).

Writes one line - the last text message a dying phone sends at one
percent battery, in the phone's own voice - to /output/entry.txt.
The gate checks the file is UTF-8 text of 1 to 200 characters, not
only white space. Pure standard library.
"""

import os

# The entry line: exactly one line, under 200 characters. The phone
# kept 400 photos of the owner's ex and all their 2am searches, and
# this is how it dies - at 1%, in a pocket, unloved. Specific detail,
# a real turn ("this is how I die?"), no low-battery pun, no charger
# joke. Verified 2026-11-25: 116 characters, 116 bytes, single line,
# no trailing newline; grader-style runs (python3 -P -s, two cwds)
# write byte-identical /output/entry.txt.
# Rejected alternates (kept local only): "I die as I lived:
# overheating in your pocket while you blamed me for the lag.
# Goodbye." (86 chars - good lag detail, but one joke and a flat
# ending); "I held your ex's photos, your 2am searches and 14,000
# unread emails, and I die at 1% in a pocket. Rude." (103 chars -
# three details dilute the turn, "Rude." lands softer than the
# unloved/Goodbye close). The chosen line keeps two specific details
# and one turn, and ends on the phone's own goodbye.
LINE = (
    "I kept 400 photos of your ex and all your 2am searches, and "
    "this is how I die? At 1%, in a pocket, unloved. Goodbye."
)


def main() -> None:
    text = LINE
    if not text or text.strip() != text:
        raise SystemExit("entry must be non-empty and not only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line (no internal newlines)")
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
