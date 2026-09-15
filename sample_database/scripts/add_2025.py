#!/usr/bin/env python3

from pathlib import Path
import sys


def main():
    current_dir = Path(f"{sys.argv[1]}")

    # Find yaml/yml files in current directory
    yaml_files = sorted(
        list(current_dir.glob("*.yaml")) +
        list(current_dir.glob("*.yml"))
    )

    if not yaml_files:
        print("No YAML files found.")
        return

    print(f"Found {len(yaml_files)} YAML files.\n")

    n_changed = 0
    n_unchanged = 0

    for path in yaml_files:

        # Remove suffix (.yaml or .yml)
        stem = path.stem

        # Already ends with _2025
        if stem.endswith("_2025"):
            print(f"[OK]      {path.name}")
            n_unchanged += 1
            continue

        # Construct new filename
        new_name = f"{stem}_2025{path.suffix}"
        new_path = path.with_name(new_name)

        # Safety check
        if new_path.exists():
            print(
                f"[WARNING] {path.name} -> {new_name} "
                f"(target already exists, skipped)"
            )
            continue

        path.rename(new_path)

        print(f"[RENAMED] {path.name} -> {new_name}")
        n_changed += 1

    print("\n" + "=" * 60)
    print(f"Total     : {len(yaml_files)}")
    print(f"Renamed   : {n_changed}")
    print(f"Unchanged : {n_unchanged}")


if __name__ == "__main__":
    main()