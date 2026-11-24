"""Write the one-line excuse to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR)."""

import os

LINE = "I delegated it to a subagent, who delegated it to a subagent, who delegated it to a subagent that just asked me for an extension."

# The gate requires 1 to 160 characters of UTF-8 text, not only whitespace.
assert 1 <= len(LINE) <= 160, len(LINE)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
