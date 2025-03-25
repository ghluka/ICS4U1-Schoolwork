import os
import random
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.images import Image, Image_File, Pixel, clean_up


def pixelate(img: Image) -> Image:
    img = img.copy()

    for row in range(0, img.get_height(), 2):
        for col in range(0, img.get_width(), 2):
            avg_r, avg_g, avg_b = [], [], []

            for y in range(0, min(2, img.get_height() - row)):
                for x in range(0, min(2, img.get_width() - col)):
                    avg_r.append(img.get_pixel(col + x, row + y).get_r())
                    avg_g.append(img.get_pixel(col + x, row + y).get_g())
                    avg_b.append(img.get_pixel(col + x, row + y).get_b())

            avg = Pixel(round(sum(avg_r) / len(avg_r)),
                        round(sum(avg_g) / len(avg_g)),
                        round(sum(avg_b) / len(avg_b)))

            for y in range(0, min(2, img.get_height() - row)):
                for x in range(0, min(2, img.get_width() - col)):
                    img.set_pixel(col + x, row + y, avg)

    return img

if __name__ == "__main__":
    bird = Image_File("data/images/lorikeet.bmp")

    pixelated_bird = pixelate(bird)
    pixelated_bird.show()

    clean_up()
