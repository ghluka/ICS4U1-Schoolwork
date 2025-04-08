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

PATH = "/".join(__file__.replace("\\", "/").split("/")[:-1])


def old_timer(img: Image) -> Image:
    """Returns a tinted copy of the Image argument that looks like it is "old fashioned".
    The applied tint the following transformation to every pixel's RGB values: 
        (R, G, B) -> (0.39R + 0.77G + 0.19B, 0.35R + 0.69G + 0.17B, 0.27R + 0.53G + 0.13B) 
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
    bar_width = img.get_width() // cuts

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


def linear_chroma_cycle(img: Image, start: Pixel, end: Pixel, n: int = 16) -> Image_Sequence:
    """Returns a new Image Sequence with 2*n (wherein n > 2) frames.
    It transitions linearly from a starting colour to an end colour,
    each colour in the transition is applied to the provided Image as a filter
    where the luminance is determined by the formula:
        (R, G, B) -> 0.298936021293775R + 0.587043074451121G + 0.114020904255103B
    The filter is applied to each frame, where every pixel is changed to the
    luminance of each pixel, multiplied by the colour in the transition.
    This transition lasts n frames, then it replays those n frames in reverse
    to achieve a smooth, infinite loop effect.
    """
    frames:list[Image] = []

    targets:list[Pixel] = []
    for i in range(max(2, n)):
        targets.append(Pixel(
            round(start.get_r() + (end.get_r() - start.get_r()) * (i / (n - 1))),
            round(start.get_g() + (end.get_g() - start.get_g()) * (i / (n - 1))),
            round(start.get_b() + (end.get_b() - start.get_b()) * (i / (n - 1))),
        ))

    for target in targets:
        frame = img.copy()

        for row in range(0, img.get_height()):
            for col in range(0, img.get_width()):
                pix = img.get_pixel(col, row)

                # grayscale value by weighted sum of the R, G, and B components
                # weights were taken from MATLAB's rgb2gray function
                brightness = 0.298936021293775 * pix.get_r() + \
                    0.587043074451121 * pix.get_g() + \
                    0.114020904255103 * pix.get_b()

                frame.set_pixel(col, row, Pixel(
                    round(brightness / 255 * target.get_r()),
                    round(brightness / 255 * target.get_g()),
                    round(brightness / 255 * target.get_b())
                ))

        frames.append(frame)

    # add all frames to image sequence
    seq = Image_Sequence()

    frames.extend(reversed(frames))

    for frame in frames:
        seq.add_image(frame)

    return seq


def radial_gradient(width:int, height:int, start:Pixel, end:Pixel) -> Image:
    img = Image_New(width, height)

    mid_x = math.floor(width // 2)
    mid_y = math.floor(height // 2)

    n = ((mid_y)**2 + (mid_x)**2) ** .5

    for row in range(0, height):
        for col in range(0, width):
            dist = ((row - mid_y)**2 + (col - mid_x)**2) ** .5

            pix = Pixel(
                max(0, min(255, round(start.get_r() + (end.get_r() - start.get_r()) * (dist / (n - 1))))),
                max(0, min(255, round(start.get_g() + (end.get_g() - start.get_g()) * (dist / (n - 1))))),
                max(0, min(255, round(start.get_b() + (end.get_b() - start.get_b()) * (dist / (n - 1))))),
            )

            img.set_pixel(col, row, pix)

    return img

if __name__ == "__main__":
    lorikeet = Image_File("data/images/lorikeet.bmp")

    lcc = linear_chroma_cycle(lorikeet, Pixel(138, 35, 135), Pixel(242, 113, 33), 32)
    lcc_2 = linear_chroma_cycle(lorikeet, Pixel(255, 0, 255), Pixel(255, 0, 0))
    lcc.play(60)
    lcc_2.play(24)
    
    rg = radial_gradient(370, 250, Pixel(255, 255, 255), Pixel(255, 255, 255))
    rg_2 = radial_gradient(720, 720, Pixel(222, 223, 221), Pixel(222, 220, 0))
    rg.show()
    rg_2.show()

    clean_up()
