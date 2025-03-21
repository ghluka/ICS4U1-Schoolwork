import os
import random
import sys
import time

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.images import WHITE, Image, Image_File


def hide_some(img: Image, percentage: float) -> Image:
    """Returns a new altered Image of the given one where a percentage of the
    image's pixels are randomly set to white.
    """
    img = img.copy()

    pixels = []
    for row in range(0, img.get_height()):
        for col in range(0, img.get_width()):
            pixels.append((col, row))

    for _ in range(round(len(pixels) * percentage)):
        i = random.randrange(len(pixels))
        pix = pixels.pop(i)

        img.set_pixel(*pix, WHITE)

    return img

if __name__ == "__main__":
    lorikeet = Image_File("data/images/lorikeet.bmp")

    start = time.perf_counter()
    hidden = hide_some(lorikeet, 0.3)
    elapsed = time.perf_counter() - start

    print(f"Took {elapsed:.6f} seconds to hide {1 - hidden.compare(lorikeet):%} of lorikeet.bmp")

    hidden.show()
