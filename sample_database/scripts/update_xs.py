#!/usr/bin/env python3

import argparse
import re
import sys
from pathlib import Path

# ------------------------------------------------------------
# Load xs.py
# ------------------------------------------------------------
try:
    from xs import xs
except ImportError:
    print("ERROR: Cannot import xs.py")
    print("Make sure xs.py is in the same directory as this script,")
    print("or is available in PYTHONPATH.")
    sys.exit(1)


def find_matching_tag(filename, xs_dict):
    """
    Find xs.py tags contained in the YAML filename.

    If multiple tags match, use the longest one.
    This avoids problems when one tag is a substring of another.
    """
    matches = []

    for tag in xs_dict:
        if tag in filename:
            matches.append(tag)

    if not matches:
        return None

    return max(matches, key=len)


def replace_xsec(path, new_xsec):
    """
    Replace only the xsec line in the YAML file,
    preserving the rest of the file.
    """

    text = path.read_text()

    # Match:
    # xsec: 0.003
    # xsec: 1.39
    # xsec: 1.23e-4
    pattern = r"(?m)^(\s*xsec\s*:\s*)[^\n#]+"

    match = re.search(pattern, text)

    if not match:
        print(f"  WARNING: no xsec field found in {path}")
        return False

    old_line = match.group(0)
    prefix = match.group(1)

    # Use a clean numeric representation
    new_value = repr(float(new_xsec))

    new_line = prefix + new_value

    if old_line == new_line:
        print(f"  unchanged: {old_line}")
        return False

    new_text = text[:match.start()] + new_line + text[match.end():]

    path.write_text(new_text)

    print(f"  {old_line.strip()}  ->  {new_line.strip()}")

    return True


def main():

    parser = argparse.ArgumentParser(
        description="Replace YAML xsec values using xs.py"
    )

    parser.add_argument(
        "directory",
        help="Directory containing YAML files"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only show what would be changed, do not modify files"
    )

    args = parser.parse_args()

    yaml_dir = Path(args.directory)

    if not yaml_dir.is_dir():
        print(f"ERROR: directory does not exist: {yaml_dir}")
        sys.exit(1)

    # Find YAML files
    yaml_files = sorted(
        list(yaml_dir.glob("*.yaml")) +
        list(yaml_dir.glob("*.yml"))
    )

    if not yaml_files:
        print(f"No YAML files found in {yaml_dir}")
        return

    print(f"Found {len(yaml_files)} YAML files")
    print(f"Found {len(xs)} cross section tags in xs.py")
    print()

    n_matched = 0
    n_changed = 0
    n_unmatched = 0

    for path in yaml_files:

        filename = path.name

        tag = find_matching_tag(filename, xs)

        print(f"{filename}")

        if tag is None:
            print("  NO MATCH")
            n_unmatched += 1
            continue

        n_matched += 1

        value = xs[tag]

        print(f"  matched tag : {tag}")
        print(f"  xs          : {value}")

        if args.dry_run:
            print("  DRY RUN: file not modified")
        else:
            if replace_xsec(path, value):
                n_changed += 1

        print()

    print("=" * 60)
    print(f"Total YAML files : {len(yaml_files)}")
    print(f"Matched          : {n_matched}")
    print(f"Unmatched        : {n_unmatched}")

    if not args.dry_run:
        print(f"Changed          : {n_changed}")


if __name__ == "__main__":
    main()