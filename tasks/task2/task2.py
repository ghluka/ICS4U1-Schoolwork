"""Provides solutions for the 2 classes in task 1's assignment
"""
import os
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.images import Image, Image_File, Pixel, clean_up, pygame

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

            R, G, B = pix.get_r(), pix.get_g(), pix.get_b()

            pix.set_r(min(round(0.39*R + 0.77*G + 0.19*B), 255))
            pix.set_g(min(round(0.35*R + 0.69*G + 0.17*B), 255))
            pix.set_b(min(round(0.27*R + 0.53*G + 0.13*B), 255))

            img.set_pixel(col, row, pix)

    return img


#def avg_distance_to(img: Image, colour: Pixel) -> float:
#    

if __name__ == "__main__":
    lorikeet = Image_File("data/images/lorikeet.bmp")

    old = old_timer(lorikeet)
    print(" old_timer():", "✅ PASSED" if old.compare(Image_File(f"{PATH}/old_timer_sample.bmp")) == 1.0 else "❌ FAILED")

    colour = Pixel(20, 100, 222)
    av_dist = avg_distance_to(lorikeet, colour)

    clean_up()
