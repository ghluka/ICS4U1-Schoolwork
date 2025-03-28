'''
Personal utility functions, do NOT submit something with these being used
'''

import os
import threading
import time

from utils.images import Image


def better_show(img: Image) -> None:
    """The provided show function doesn't allow for zooming in and out,
    this just allows for me to open an image in the Paint program so I can
    further analyze an image.
    """
    img.save()
    os.startfile("temp.bmp")
    time.sleep(1)
    os.remove("temp.bmp")
