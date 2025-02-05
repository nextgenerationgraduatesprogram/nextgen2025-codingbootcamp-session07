import os
import sys
import argparse
from pathlib import Path
from omegaconf import OmegaConf
from typing import *

# add path of `src` to sys.path
from dotenv import load_dotenv
load_dotenv(".env")
PROJECT_ROOT = os.environ["PROJECT_ROOT"]
sys.path.append(PROJECT_ROOT)

# import your libraries
from src.datasets import FashionMnist


def main(args: List[str]) -> Any:
    # parse the args
    args, unknown_args = parse_args(args)

    # load the configuration for the dataset
    args.dataset = Path(PROJECT_ROOT).joinpath("configs").joinpath(args.dataset)
    cfg = OmegaConf.load(args.dataset)

    # load overrides and merge
    overrides = OmegaConf.from_dotlist(unknown_args)
    cfg = OmegaConf.merge(cfg, overrides)

    # load the configuration and build the dataset
    # NOTE: we need to be careful about types with overrides : can cause a bit of a headache
    # print(cfg.regex, type(cfg.regex)) # want a str
    dataset = FashionMnist(cfg.root, str(cfg.regex))

    # apply the process to the dataset
    for idx, (img, lbl) in enumerate(dataset):
        print(f"img {img.shape} with label {lbl}")


def parse_args(args: List[str]) -> Tuple[List[str], List[str]]:
    # define the parser
    parser = argparse.ArgumentParser(
        description="Downloads and processes the FashionMNIST dataset.",
        epilog="Please contact sam.cantrill@data61.csiro.au for further help."
    )
    parser.add_argument("--dataset",
        required=True,
        type=str,
        help="Configuration file to use for the dataset."
    )

    # define the system arguments
    args, unknow_args = parser.parse_known_args(args)

    return args, unknow_args


if __name__ == "__main__":
    main(sys.argv[1:])


