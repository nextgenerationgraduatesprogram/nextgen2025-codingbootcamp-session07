import os
import sys
import cv2
import hydra
from pathlib import Path
from omegaconf import DictConfig, OmegaConf
from typing import *

# add path of `src` to sys.path
from dotenv import load_dotenv
load_dotenv(".env")
sys.path.append(os.environ["PROJECT_ROOT"])

# import your libraries
from src.datasets import FashionMnist
from src.processes import Rotate


@hydra.main(version_base=None, config_path=str(Path(os.environ["PROJECT_ROOT"]).joinpath("configs")), config_name="default")
def main(cfg: DictConfig) -> None:
    # lets show the hydra config
    print(OmegaConf.to_yaml(cfg))

    # load the configuration and build the dataset
    # NOTE: we need to be careful about types with overrides : can cause a bit of a headache
    dataset = FashionMnist(cfg.dataset.root, str(cfg.dataset.regex))

    # load the processes to be applied to the item
    process = Rotate(int(cfg.process.rotation))

    # apply the process to the dataset
    for idx, (img, lbl) in enumerate(dataset):
        # rotate the image
        img = process(img)

        # save the image
        cv2.imwrite(Path(cfg.paths.artifacts).joinpath(f"{idx}.png"), img)

    # write some metadata bout the job
    if "note" in cfg:
        with open(Path(cfg.paths.artifacts).joinpath("note.txt"), "w") as f:
            f.write(cfg.note)

if __name__ == "__main__":
    main()

