import os
import cv2
import sys
import argparse
from uuid import uuid4
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
from src.processes import Rotate


def main(args: List[str]) -> Any:
    # parse the args
    cfg = parse_args(args)

    # define the uuid to use to reference specific artifacts
    # NOTE : we can override the cfg values
    cfg.artifacts = Path(cfg.artifacts).joinpath(str(uuid4()))
    cfg.artifacts.mkdir(exist_ok=False, parents=True) # want to raise error if it exists (highly unlikeyly)
    print(f"exporting artifacts to {cfg.artifacts}")

    # load the configuration and build the dataset
    # NOTE: we need to be careful about types with overrides : can cause a bit of a headache
    dataset = FashionMnist(cfg.root, str(cfg.regex))

    # load the processes to be applied to the item
    process = Rotate(int(cfg.rotation))

    # apply the process to the dataset
    for idx, (img, lbl) in enumerate(dataset):
        print(f"img {img.shape} with label {lbl}")

        # rotate the image
        img = process(img)

        # save the image
        cv2.imwrite(cfg.artifacts.joinpath(f"{idx}.png"), img)

    # we can even write some metadata if we want about it
    if "note" in cfg:
        with open(cfg.artifacts.joinpath("note.txt"), "w") as f:
            f.write(cfg.note)


def parse_args(args: List[str]) -> Tuple[List[str], List[str]]:
    # define the parser
    parser = argparse.ArgumentParser(
        description="Downloads and processes the FashionMNIST dataset.",
        epilog="Please contact sam.cantrill@data61.csiro.au for further help."
    )
    parser.add_argument("--dataset",
        required=False,
        default="dataset_A.yaml",
        choices=[
            "dataset_A.yaml",
            "dataset_B.yaml"
        ],
        type=str,
        help="Configuration file to use for the dataset."
    )
    parser.add_argument("--process",
        required=False,
        default="process_A.yaml",
        choices=[
            "process_A.yaml"
        ],
        type=str,
        help="Configuration file to use for the dataset."
    )
    parser.add_argument("--paths",
        required=False,
        default="paths.yaml",
        type=str,
        help="Configuration file to use for paths."
    )

    # define the system arguments
    args, unknow_args = parser.parse_known_args(args)

    # parse args into configs : load the configurations from each file
    cfg = None
    cfg_dir = Path(PROJECT_ROOT).joinpath("configs")
    for key, val in vars(args).items():
        _loaded = OmegaConf.load(cfg_dir.joinpath(val))
        print(f"loaded {val} from {key}")
        cfg = OmegaConf.merge(cfg,_loaded) if cfg is not None else _loaded

    # load overrides and merge
    overrides = OmegaConf.from_dotlist(unknow_args)
    cfg = OmegaConf.merge(cfg, overrides)

    return cfg


if __name__ == "__main__":
    main(sys.argv[1:])


