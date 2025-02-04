import cv2
import gzip
import urllib
from urllib import request
import numpy as np
from pathlib import Path

from typing import *


def download_fashion_mnist(output_path: str, num_samples : Optional[int] = 10) -> str:
    # URLs for MNIST dataset
    base_url = "http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/"
    files = {
        "test_images": "t10k-images-idx3-ubyte.gz",
        "test_labels": "t10k-labels-idx1-ubyte.gz"
    }

    # validate the output directory
    output_path = Path(output_path).absolute().resolve()
    output_path.mkdir(exist_ok=True, parents=True)

    # Download the files
    for key, filename in files.items():
        src = base_url + filename # source url
        dst = output_path.joinpath(filename) # destination file
        if not dst.exists():
            request.urlretrieve(src, dst)

    # extract the images and save them
    imgs = output_path.joinpath(files["test_images"])
    with gzip.open(imgs, "rb") as file:
        imgs = np.frombuffer(file.read(), np.uint8, offset=16)
        imgs = imgs.reshape(-1,28,28) # [N,28,28]

    # extract the labels and save them
    lbls = output_path.joinpath(files["test_labels"])
    with gzip.open(lbls, "rb") as file:
        lbls = np.frombuffer(file.read(), np.uint8, offset=8) # [N]
        
    # lets export them into a specific structure : just use the first 10 for the sake of it
    for idx in range(num_samples):
        # create a subdirectory
        idx_dir = output_path.joinpath("fashion_mnist").joinpath(str(idx))
        idx_dir.mkdir(exist_ok=True, parents=True)

        # save the image using cv2
        cv2.imwrite(idx_dir.joinpath(f"img.png"), imgs[idx])

        # save the labe in plain text
        with open(idx_dir.joinpath("label.txt"), "w") as f:
            f.writelines([str(lbls[idx])])

    return output_path.joinpath("fashion_mnist")
