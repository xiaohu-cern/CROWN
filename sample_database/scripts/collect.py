#!/usr/bin/env python3

import argparse
from pathlib import Path
import yaml
from yaml.emitter import Emitter


def main():

    parser = argparse.ArgumentParser(
        description="Merge YAML files into a dictionary keyed by nick"
    )

    parser.add_argument(
        "input_dir",
        help="Directory containing YAML files"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="merged.yaml",
        help="Output YAML file (default: merged.yaml)"
    )

    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_file = Path(args.output)

    if not input_dir.is_dir():
        print(f"ERROR: directory does not exist: {input_dir}")
        return

    # yaml_files = sorted(
    #     list(input_dir.glob("*.yaml")) +
    #     list(input_dir.glob("*.yml"))
    # )
    yaml_files = sorted(
        list(input_dir.rglob("*.yaml")) +
        list(input_dir.rglob("*.yml"))
    )

    # Don't read output file if it is inside input_dir
    yaml_files = [
        f for f in yaml_files
        if f.resolve() != output_file.resolve()
    ]

    if not yaml_files:
        print(f"No YAML files found in {input_dir}")
        return

    merged = {}

    for yaml_file in yaml_files:

        print(f"Reading: {yaml_file.name}")

        with open(yaml_file, "r") as f:
            data = yaml.safe_load(f)

        if data is None:
            print("  WARNING: empty file, skipped")
            continue

        if not isinstance(data, dict):
            print("  WARNING: unexpected YAML structure, skipped")
            continue

        # Get nick
        nick = data.get("nick")

        if not nick:
            print("  WARNING: no 'nick' found, skipped")
            continue

        # Remove filelist
        data.pop("filelist", None)

        # Make nick the first item in the block
        new_data = {
            "nick": nick
        }

        # Add all remaining fields while preserving their original order
        for key, value in data.items():
            if key != "nick":
                new_data[key] = value

        # Use nick as the top-level key
        if nick in merged:
            print(f"  WARNING: duplicate nick '{nick}', overwriting")

        # merged[nick] = new_data
        merged[str(nick)] = new_data

    # Write output
    # with open(output_file, "w") as f:
    #     # yaml.safe_dump(
    #     #     merged,
    #     #     f,
    #     #     sort_keys=False,
    #     #     default_flow_style=False,
    #     #     allow_unicode=True,
    #     #     width=4096
    #     # )
    #     yaml.safe_dump(
    #         merged,
    #         f,
    #         sort_keys=False,
    #         default_flow_style=False,
    #         allow_unicode=True,
    #         width=float("inf")
    #     )

    with open(output_file, "w") as f:
        for nick, block in merged.items():

            # write top-level key manually
            f.write(f"{nick}:\n")

            # write content
            for key, value in block.items():

                # skip filelist if exists
                if key == "filelist":
                    continue

                # simple scalar values
                f.write(f"  {key}: {value}\n")

            f.write("\n")

    print()
    print("=" * 60)
    print(f"Input files : {len(yaml_files)}")
    print(f"Merged      : {len(merged)}")
    print(f"Output      : {output_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()