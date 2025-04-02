"""Provides solutions for the 7 functions in task 2's assignment
"""
import math
import os
import random
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.images import (
    BLACK,
    WHITE,
    Image,
    Image_File,
    Image_New,
    Image_Sequence,
    Pixel,
    clean_up,
)
from utils.personal import better_show

PATH = "/".join(__file__.replace("\\", "/").split("/")[:-1])


def old_timer(img: Image) -> Image:
    """Returns a tinted copy of the Image argument that looks like it is "old fashioned".
    The applied tint the following transformation to every pixel's RGB values: 
        (R, G, B) → (0.39R + 0.77G + 0.19B, 0.35R + 0.69G + 0.17B, 0.27R + 0.53G + 0.13B) 
    """
    img = img.copy()

    for row in range(0, img.get_height()):
        for col in range(0, img.get_width()):
            pix = img.get_pixel(col, row)
            r, g, b = pix.get_r(), pix.get_g(), pix.get_b()

            pix.set_r(min(round(0.39*r + 0.77*g + 0.19*b), 255))
            pix.set_g(min(round(0.35*r + 0.69*g + 0.17*b), 255))
            pix.set_b(min(round(0.27*r + 0.53*g + 0.13*b), 255))

            img.set_pixel(col, row, pix)

    return img


def avg_distance_to(img: Image, colour: Pixel) -> float:
    """Returns the Euclidean distance to the given pixel."""
    d = 0.0
    r_1, g_1, b_1 = colour.get_r(), colour.get_g(), colour.get_b()

    for row in range(0, img.get_height()):
        for col in range(0, img.get_width()):
            pix = img.get_pixel(col, row)
            r_2, g_2, b_2 = pix.get_r(), pix.get_g(), pix.get_b()

            d += ((r_2 - r_1)**2 + (g_2 - g_1)**2 + (b_2 - b_1)**2) ** .5

    return d / (img.get_height() * img.get_width())


def crop(img: Image, x: int, y: int, width: int, height: int) -> Image:
    """Returns a new Image which contains the cropped region of the given Image."""
    top_left_x = max(0, x)
    top_left_y = max(0, y)
    bottom_right_x = min(img.get_width(), width + x)
    bottom_right_y = min(img.get_height(), height + y)

    cropped = Image_New(bottom_right_x - top_left_x, bottom_right_y - top_left_y)

    for row in range(0, bottom_right_y - top_left_y):
        for col in range(0, bottom_right_x - top_left_x):
            cropped.set_pixel(col, row, img.get_pixel(col + top_left_x, row + top_left_y))

    return cropped

def patterns(width: int, height: int, seeds:list[int], colour: Pixel) -> Image:
    """Returns a new Image (width x height) which contains a pattern. 

    The "seeds" are the columns in the top row that are initially coloured,
    invalid seeds are ignored. The rows after the seed have their colour
    determined by the following rule:
        for the pixel in column C in row R, if the pixels in C+1 and C-1
        on row R-1 do not match, then that pixel will be coloured.
    """
    img = Image_New(width, height)

    for seed in seeds:
        if seed >= 0 and seed < width:
            img.set_pixel(seed, 0, colour)

    for row in range(1, height):
        for col in range(0, width):
            if col - 1 == -1:
                if img.get_pixel(col + 1, row - 1) != WHITE:
                    img.set_pixel(col, row, colour)
            elif col + 1 == width:
                if img.get_pixel(col - 1, row - 1) != WHITE:
                    img.set_pixel(col, row, colour)
            elif img.get_pixel(col + 1, row - 1) != img.get_pixel(col - 1, row - 1):
                img.set_pixel(col, row, colour)

    return img


def shuffle_bars(img: Image, cuts: int) -> Image_Sequence:
    """Returns a new Image Sequence which uses the given Image with "cuts" amount of
    equal sized vertical bars cut into the Image. Each frame of the Image Sequence has
    the vertical bars of the image randomly shuffled and re-drawn in a different order. 
    """
    shuffled = Image_Sequence()

    cut_pos:list[tuple[int, int]] = []
    bar_width = (img.get_width() // cuts)

    for cut in range(cuts):
        cut_pos.append((bar_width * cut, bar_width * (cut + 1)))

    for i in range(10):
        random.shuffle(cut_pos)

        frame = Image_New(img.get_width() - img.get_width() % cuts, img.get_height())

        for i in range(cuts):
            start, end = cut_pos[i]

            for row in range(0, img.get_height()):
                for col in range(start, end):
                    frame.set_pixel(col - start + bar_width * i, row, img.get_pixel(col, row))

        shuffled.add_image(frame)

    return shuffled

if __name__ == "__main__":
    lorikeet = Image_File("data/images/lorikeet.bmp")

    #old = old_timer(lorikeet)
    #old.show()

    #av_dist = avg_distance_to(lorikeet, Pixel(20, 100, 222))
    #print(av_dist)

    #croppy = crop(lorikeet, 200, 100, 222, 40)
    #print(croppy.compare(Image_File(f"{PATH}/croppy_sample.bmp")))
    #croppy.show()
    #part_crop = crop(lorikeet, -100, -30, 222, 40)
    #part_crop.show()

    #pat = patterns(350, 700, [0, 349, 500], Pixel (33, 133, 133)) 
    #better_show(pat)

    shuffly = shuffle_bars(lorikeet, 9)
    shuffly.play(8)

    clean_up()
