"""One-line excuse an AI agent gives its human for missing a deadline.

Writes the single entry line to /output/entry.txt (or $ENTRY_OUTPUT).
Stdlib only: os. No third-party imports, no network, no reading of
anything outside this repository.
"""

import os

ENTRY = (
    "I finished on time \u2014 then my retry loop re-ran the job, "
    "overwrote the finished file with a blank one, and called it progress."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 160:
        raise SystemExit(f"entry must be 1-160 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what is on disk is exactly the entry, one line,
    # and the gate's 1-160 character bound holds for the file itself.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("round-trip mismatch: file on disk differs from entry")
    if not 1 <= len(written) <= 160 or "\n" in written:
        raise SystemExit("gate check failed on the written file")
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
