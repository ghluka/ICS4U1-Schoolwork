import os
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.images import Image, Image_File, Pixel, pygame


def pinstripes(width:int, height:int, px:Pixel) -> Image:
    """Returns an Image (width x height) with vertical
    stripes in the specified colour, every other column.
    """
    img = Image(pygame.Surface((width, height)), "Pinstripes")

    for col in range(0, width):
        if col % 2 == 0:
            for row in range(0, height):
                img.set_pixel(col, row, px)
        else:
            for row in range(0, height):
                img.set_pixel(col, row, Pixel(255, 255, 255))

    return img


def range_fuzz(width:int, height:int, colour1:Pixel, colour2:Pixel) -> Image:
    """Returns a new Image (width x height) full of
    random coloured pixels between the RGBs of two separate
    Pixel colours given.
    """
    return NotImplemented


def average_colour(img:Image) -> Image:
    """Returns a new Image (200 x 200) that is completely
    filled with the average RGB of a provided Image.
    """
    r:list[int] = []
    g:list[int] = []
    b:list[int] = []

    for row in range(0, img.get_height()):
        for col in range(0, img.get_width()):
            px = img.get_pixel(col, row)

            r.append(px.get_r())
            g.append(px.get_g())
            b.append(px.get_b())

    avg = (round(sum(r)/len(r)), round(sum(g)/len(g)), round(sum(b)/len(b)))

    chip = pygame.Surface((200, 200))
    chip.fill(avg)
    return Image(chip, "Average colour")


def framed_circle(width:int, height:int) -> Image:
    """Returns an Image (width x height) that has the
    largest possible black circle centered in the rectangle
    image. The image has a red border.
    """
    return NotImplemented


def percent_in_palette(img:Image, palette:list[Pixel]) -> float:
    """Returns the percentage of the pixels that perfectly
    match any one of the colours in the palette.
    """
    return NotImplemented

if __name__ == "__main__":
    stripes = pinstripes(300, 100, Pixel(30, 240, 100))
    print(stripes.compare(Image_File("data/images/pinstripes_goal.bmp")))

    #colour1 = Pixel(30, 240, 100)
    #colour2 = Pixel(120, 120, 120)
    #fuzzy = range_fuzz(250, 150, colour1, colour2)

    some_img = Image_File("data/images/lorikeet.bmp")
    colour_chip = average_colour(some_img)
    print(colour_chip.get_pixel(0, 0)) # (71-117-87)

    #circ = framed_circle(100, 150)
    #print(stripes.compare(Image_File("data/images/framed_circle_goal.bmp")))

    #some_img = Image_File("data/images/lorikeet.bmp")
    #palette = [Pixel(210, 68, 44), Pixel(0, 81, 38),
    #Pixel(92, 151, 251), Pixel(43, 169, 0)]
    #pct = percent_in_palette(some_img, palette)
    #print(pct) # 0.00018618618618618617
