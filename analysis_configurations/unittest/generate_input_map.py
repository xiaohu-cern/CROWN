import ROOT
import argparse
import os
import json


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate a json file containing the mapping of shifts to quantities"
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        help="Input ROOT file containing the shift quantities map",
        required=True,
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        help="Output json file containing the shift quantities map",
        required=True,
    )
    return parser.parse_args()


def load_crown_mapping(filename):
    data = {}
    ROOT.gSystem.Load(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "../../code_generation",
            "maplib.so",
        )
    )
    f = ROOT.TFile.Open(filename)
    name = "shift_quantities_map"
    m = f.Get(name)
    for shift, quantities in m:
        data[str(shift)] = [str(quantity) for quantity in quantities]
    f.Close()
    print("Cleaning up autogenerated files")
    return data


args = parse_arguments()

# dump the data to a json file
data = {}
data["2018"] = {}
data["2018"]["dyjets"] = {}
for scope in ["et", "mt", "mm"]:
    data["2018"]["dyjets"][scope] = load_crown_mapping(args.input)
with open(args.output, "w") as f:
    json.dump(data, f, indent=4)
