#!/usr/bin/env python3

import sys
import os
from pathlib import Path


def main():

    if len(sys.argv) < 3:
        print(
            "Usage: python make_txt.py <output_prefix> <yaml_directory>"
        )
        sys.exit(1)

    prefix = sys.argv[1]
    yaml_dir = Path(sys.argv[2])
    txt_dir = Path(sys.argv[3])

    os.system(f"rm -rf {txt_dir}")
    os.system(f"mkdir -p {txt_dir}")
    print("Delete and initilize txt directory: ", txt_dir)

    if not yaml_dir.is_dir():
        print(f"ERROR: directory not found: {yaml_dir}")
        sys.exit(1)

    # Find yaml files
    yaml_files = sorted(yaml_dir.glob("*.yaml"))

    if not yaml_files:
        print(f"No yaml files found in {yaml_dir}")
        return


    for idx, yaml_file in enumerate(yaml_files):

        # remove .yaml
        sample_name = yaml_file.stem

        txt_name = f"{prefix}_{idx:03d}.txt"

        with open(f"{txt_dir}/{txt_name}", "w") as f:
            f.write(sample_name + "\n")

        print(
            f"{yaml_file.name} -> {txt_name}"
        )


    print()
    print(f"Created {len(yaml_files)} txt files.")


if __name__ == "__main__":
    main()