import os
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.images import Image, Image_File, Image_Sequence


def reduce(img:Image, color_component:str) -> Image:
    """Returns a new Image that has reduced just the specified colour
    component ("r", "g", or "b") of the given Image by 75% for the given image.
    """
    img = img.copy()

    for row in range(0, img.get_height()):
        for col in range(0, img.get_width()):
            pix = img.get_pixel(col, row)

            if color_component == "r":
                pix.set_r(round(pix.get_r() / 4))
            elif color_component == "g":
                pix.set_g(round(pix.get_g() / 4))
            elif color_component == "b":
                pix.set_b(round(pix.get_b() / 4))

            img.set_pixel(col, row, pix)

    return img


def brighten(img:Image, brightness_percent:float) -> Image:
    """Returns a new Image that results from brightening all
    colour components by the specified percentage in the given Image.
    """
    img = img.copy()

    for row in range(0, img.get_height()):
        for col in range(0, img.get_width()):
            pix = img.get_pixel(col, row)

            pix.set_r(min(round(pix.get_r() * (1 + brightness_percent)), 255))
            pix.set_g(min(round(pix.get_g() * (1 + brightness_percent)), 255))
            pix.set_b(min(round(pix.get_b() * (1 + brightness_percent)), 255))

            img.set_pixel(col, row, pix)

    return img


def negative(img:Image) -> Image:
    """Returns a new Image that results from the negative
    of the specified image file. All colour components of every
    pixel be flipped to the opposite side of the spectrum from 0 - 255.
    """
    img = img.copy()

    for row in range(0, img.get_height()):
        for col in range(0, img.get_width()):
            pix = img.get_pixel(col, row)

            pix.set_r(255 - pix.get_r())
            pix.set_g(255 - pix.get_g())
            pix.set_b(255 - pix.get_b())

            img.set_pixel(col, row, pix)

    return img


def mirror(img:Image) -> Image:
    """Returns a new Image that results from reflecting the
    top half of an image across its horizontal mid-line.
    """
    return mirror_sequence(img).get_frame(img.get_height() // 2 + 1)


def mirror_sequence(img:Image) -> Image_Sequence:
    """Returns an Image_Sequence object that contains the
    resulting Images from reflecting the top half of an image
    across its horizontal mid-line, one row at a time.
    """
    img = img.copy()
    img_sequence = Image_Sequence()

    for row in range(img.get_height() // 2, img.get_height()):
        for col in range(0, img.get_width()):
            img.set_pixel(col, row, img.get_pixel(col, img.get_height() - row))
        img_sequence.add_image(img.copy())

    return img_sequence

if __name__ == "__main__":
    sample = Image_File("data/images/lorikeet.bmp")

    less_green = reduce(sample, "g")
    less_green.show()

    bright_20 = brighten(sample, 0.2)
    bright_20.show()

    neg_image = negative(sample)
    neg_image.show()

    mirrored_image = mirror(sample)
    mirrored_image.show()

    mirror_seq = mirror_sequence(sample)
    mirror_seq.play(20)
