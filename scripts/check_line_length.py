import sys
from pathlib import Path


def check_line_length(path, max_length=119):
    """
    Checks if any line in the file at `path` exceeds `max_length` characters.
    Returns a list of (line_number, line_content) for offending lines.
    """
    offending = []
    with open(path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if len(line.rstrip('\n')) > max_length:
                offending.append((i, line.rstrip('\n')))
    return offending


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_line_length.py <file_or_directory> [max_length]")
        sys.exit(1)
    target = Path(sys.argv[1])
    max_length = int(sys.argv[2]) if len(sys.argv) > 2 else 119
    files = []
    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = list(target.rglob('*.py'))
    else:
        print(f"{target} is not a valid file or directory.")
        sys.exit(1)
    any_offending = False
    for file in files:
        offending = check_line_length(file, max_length)
        if offending:
            any_offending = True
            print(f"{file}:")
            for line_num, content in offending:
                print(f"  Line {line_num}: {content}")
    if not any_offending:
        print("All lines within limit.")


if __name__ == "__main__":
    main()
