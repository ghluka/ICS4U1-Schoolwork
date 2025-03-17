import os
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.images import Image, Image_File, Image_Sequence


def neon(img: Image) -> Image:
    """
    Creates a neon-type filter on the given Image and returns the result.
    """
    img = img.copy()

    for row in range(0, img.get_height()):
        for col in range(0, img.get_width()):
            pix = img.get_pixel(col, row)

            pix.set_r(round(pix.get_r() / 2))
            pix.set_g(255 - pix.get_g())
            pix.set_b(min(round(pix.get_b() * 1.5), 255))

            img.set_pixel(col, row, pix)

    return img


def slide(img: Image, distance: int) -> Image:
    """
    Horizontally slides the given image by the given distance,
    returning the resulting image. The translated image 'wraps around'
    to the other side. This can handle any integer value for distance.
    """
    pass


def x_box(width: int) -> Image:
    """
    Returns a square image of the given width with a black 'X'
    connecting opposite corners.
    """
    pass



def slide_sequence(img: Image, distance: int) -> Image_Sequence:
    """
    Horizontally slides the given image by the given distance.
    The translated image 'wraps around' to the other side.
    This can handle any integer value for distance.
    The sequence of images returned contains separate frames incrementing
    the distance by 10 pixels each, animating the full slide.
    """
    pass


if __name__ == "__main__":
    #Test the code:
    im = Image_File("data/images/lorikeet.bmp")
    w = neon(im)

    #w.save("neon.bmp")
    w.show()

    #x = x_box(255)
    #x.save("x_box_255.bmp")
    #x.show()

    #x = x_box(200)
    #x.save("x_box_200.bmp")
    #x.show()


    #s = slide(im, 140)
    #s.save("slide_140.bmp")
    #s.show()


    #im.show() #<-- shows the original image was unchanged

    #ss = slide_sequence(im, 140)
    #ss.play(10)


    #this will close any lingering Pygame windows (from using 'run')
    #clean_up()
