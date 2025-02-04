import cv2
from pathlib import Path
from src.utils import download_fashion_mnist

from typing import *
from numpy import ndarray


class FashionMnist:
    def __init__(self, 
        root: str, 
        regex: Optional[str] = None,
    ) -> None:
        super(FashionMnist, self).__init__()

        # download into root and return the new root
        root : str = download_fashion_mnist(root)
        print(f"downloaded fashion_mnist into root")
        self.samples = list(Path(root).glob(regex)) # index the items on init

        # validate
        assert Path(root).exists(), f"provided root does not exist"
        assert len(self) > 0, f"no items exist in the dataset, check the regex"

    def __len__(self) -> int:
        """
        enables us to self len(dataset) to get the number of items in the dataset
        """
        return len(self.samples)

    def __getitem__(self, index: int) -> Tuple[Any, str]:
        """
        enables us to index into the dataset using dataset[index] to get a specific item
        """
        # index the relevant sample
        sample = self.samples[index]

        # define filepaths
        img_filepath : Path = sample.joinpath("img.png")
        lbl_filepath : Path = sample.joinpath("label.txt")

        # load data
        img : ndarray = self.read_image(img_filepath)
        lbl : int = self.read_label(lbl_filepath)

        # return data
        return img, lbl

    def __iter__(self) -> Tuple[Any, str]:
        """
        enables us to iterate over the dataset
        """
        # iterate over the samples in our dataset
        for idx in range(len(self)):
            # index the data using `__getitem__`
            img, lbl = self.__getitem__(idx)

            # yield the data
            yield img, lbl

    def read_image(self, path: str) -> ndarray:
        img : ndarray = cv2.imread(path)
        return img

    def read_label(self, path: str) -> int:
        with open(path, "r") as file:
            data : int = int(file.read())
        return data
