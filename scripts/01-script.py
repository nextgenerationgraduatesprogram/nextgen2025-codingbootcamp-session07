import os
import sys
import argparse
from pathlib import Path
from typing import *

# add path of `src` to sys.path
from dotenv import load_dotenv
load_dotenv(".env")
sys.path.append(os.environ["PROJECT_ROOT"])

# import your libraries
from src.datasets import FashionMnist


def main(args: List[str]) -> Any:
    # parse the args
    args, unknown_args = parse_args(args)

    # load the configuration and build the dataset
    dataset = FashionMnist(args.root, args.regex)

    # apply the process to the dataset
    for idx, (img, lbl) in enumerate(dataset):
        print(f"img {img.shape} with label {lbl}")


def parse_args(args: List[str]) -> Tuple[List[str], List[str]]:
    # define the parser
    parser = argparse.ArgumentParser(
        description="Downloads and processes the FashionMNIST dataset.",
        epilog="Please contact sam.cantrill@data61.csiro.au for further help."
    )
    parser.add_argument("--root",
        required=True,
        type=str,
        help="Root directory to store the dataset into."
    )
    parser.add_argument("--regex",
        required=False,
        type=str,
        default="*",
        help="Regular expression to use for matching samples in the dataset."
    )

    # define the system arguments
    args, unknow_args = parser.parse_known_args(args)

    return args, unknow_args


if __name__ == "__main__":
    main(sys.argv[1:])


