import os
import random
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.images import Image, Image_File, Image_New, Pixel, clean_up


def blend_two(img1: Image, img2: Image) -> Image:
    new_img = Image_New(img1.get_width(), img1.get_height())

    for row in range(0, img1.get_height()):
        for col in range(0, img1.get_width()):
            pix1 = img1.get_pixel(col, row)
            pix2 = img2.get_pixel(col, row)

            red = round((pix1.get_r()+pix2.get_r())/2)
            green = round((pix1.get_g()+pix2.get_g())/2)
            blue = round((pix1.get_b()+pix2.get_b())/2)

            avg = Pixel(red, green, blue)

            new_img.set_pixel(col, row, avg)

    return new_img


def corners(img1: Image, img2: Image) -> Image:
    new_img = Image_New(img1.get_width(), img1.get_height())

    for row in range(0, img1.get_height()):
        for col in range(0, img1.get_width()):
            if row >= img1.get_height() // 2 and col >= img1.get_width() // 2 or \
                row <= img1.get_height() // 2 and col <= img1.get_width() // 2:
                pix = img1.get_pixel(col, row)
            else:
                pix = img2.get_pixel(col, row)
            
            new_img.set_pixel(col, row, pix)

    return new_img

if __name__ == "__main__":
    bird = Image_File("data/images/lorikeet.bmp")
    dog = Image_File("data/images/dog.jpg")

    bird_dog_blend = blend_two(bird, dog)
    bird_dog_blend.show()

    bird_dog_corners = corners(bird, dog)
    bird_dog_corners.show()

    clean_up()
