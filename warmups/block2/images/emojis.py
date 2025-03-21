import os
import random
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.images import WHITE, Image, Image_File, Image_New, Image_Sequence


def emojis(emoji1: Image, emoji2: Image, width: int, height: int, n: int) -> Image:
    img = Image_New(width, height)

    for i in range(n):
        ran_x = random.randrange(0, width)
        ran_y = random.randrange(0, height)

        emoji = emoji1
        if random.randrange(0, 2) == 1:
            emoji = emoji2

        for row in range(ran_y, min(emoji.get_height() + ran_y, height)):
            for col in range(ran_x, min(emoji.get_width() + ran_x, width)):
                pix = emoji.get_pixel(col - ran_x, row - ran_y)

                if pix != WHITE:
                    img.set_pixel(col, row, pix)

    return img


def emoji_seq(emoji1: Image, emoji2: Image, width: int, height: int, n: int) -> Image_Sequence:
    seq = Image_Sequence()
    img = Image_New(width, height)

    for i in range(n):
        ran_x = random.randrange(0, width)
        ran_y = random.randrange(0, height)

        emoji = emoji1
        if random.randrange(0, 2) == 1:
            emoji = emoji2

        for row in range(ran_y, min(emoji.get_height() + ran_y, height)):
            for col in range(ran_x, min(emoji.get_width() + ran_x, width)):
                pix = emoji.get_pixel(col - ran_x, row - ran_y)

                if pix != WHITE:
                    img.set_pixel(col, row, pix)
        
        seq.add_image(img.copy())

    return seq

if __name__ == "__main__":
    emoji1 = Image_File("data/images/smiley.png")
    emoji2 = Image_File("data/images/nauseated.png")
    
    em = emojis(emoji1, emoji2, 600, 400, 80)
    em.show()

    ems = emoji_seq(emoji1, emoji2, 600, 400, 80)
    ems.play(15)
