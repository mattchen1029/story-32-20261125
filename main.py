import os

WIFI_NAME = "TheRouterIsInTheDivorcePapers"

MIN_CHARS = 1
MAX_CHARS = 32
OUTPUT_NAME = "entry.txt"


def validate_name(name):
    if not (MIN_CHARS <= len(name) <= MAX_CHARS):
        raise ValueError("name must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(name)))
    if "\n" in name or "\r" in name:
        raise ValueError("name must be a single line")
    if not name.strip():
        raise ValueError("name must not be only whitespace")


def write_entry(name, out_dir):
    validate_name(name)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_NAME), "w", encoding="utf-8") as f:
        f.write(name)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(WIFI_NAME, out_dir)


if __name__ == "__main__":
    main()
