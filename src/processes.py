import cv2

from typing import *
from numpy import ndarray


class Rotate:
    def __init__(self, rotation: int) -> None:
        super(Rotate, self).__init__()
        self.rotation = rotation

    def __call__(self, img: ndarray, *args, **kwds):
        x, y = img.shape[0:2] # H, W, C
        m = cv2.getRotationMatrix2D((y,x), self.rotation, 1)
        img = cv2.warpAffine(img, m, (y,x))
        return img