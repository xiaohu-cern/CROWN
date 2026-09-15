#!/usr/bin/env python3

import argparse
import yaml


def compare_blocks(yaml1, yaml2):

    with open(yaml1, "r") as f:
        data1 = yaml.safe_load(f)

    with open(yaml2, "r") as f:
        data2 = yaml.safe_load(f)

    if data1 is None:
        data1 = {}

    if data2 is None:
        data2 = {}

    keys1 = set(data1.keys())
    keys2 = set(data2.keys())

    print("=" * 80)

    # Compare block names
    only1 = keys1 - keys2
    only2 = keys2 - keys1

    if only1:
        print("\nOnly in first file:")
        for k in sorted(only1):
            print("  ", k)

    if only2:
        print("\nOnly in second file:")
        for k in sorted(only2):
            print("  ", k)


    common = keys1 & keys2

    different = []

    for key in sorted(common):

        block1 = data1[key]
        block2 = data2[key]

        # dictionary comparison ignores order automatically
        if block1 != block2:
            different.append(key)

            print("\n" + "-" * 80)
            print(f"Different block: {key}")

            print("\nFirst:")
            print(yaml.dump(
                block1,
                sort_keys=False,
                default_flow_style=False
            ))

            print("Second:")
            print(yaml.dump(
                block2,
                sort_keys=False,
                default_flow_style=False
            ))


    print("\n" + "=" * 80)
    print(f"Total blocks in first : {len(keys1)}")
    print(f"Total blocks in second: {len(keys2)}")
    print(f"Common blocks         : {len(common)}")
    print(f"Different blocks      : {len(different)}")



def main():

    parser = argparse.ArgumentParser(
        description="Compare two datasets.yaml files"
    )

    parser.add_argument(
        "yaml1",
        help="First datasets.yaml"
    )

    parser.add_argument(
        "yaml2",
        help="Second datasets.yaml"
    )

    args = parser.parse_args()

    compare_blocks(args.yaml1, args.yaml2)


if __name__ == "__main__":
    main()