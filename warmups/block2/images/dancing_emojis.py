import os
import random
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.images import WHITE, Image, Image_File, Image_New, Image_Sequence

MOVEMENT = [-10, 10] # how much we allow the emojis to translate


class Emoji(object):
    """Class that models an Emoji with an x and y coordinate, and an Image."""
    def __init__(self, x:int, y:int, emoji:Image):
        self.__emoji = emoji
        self.x = x
        self.y = y
    
    def get_emoji(self) -> Image:
        """Accessor for the class' emoji Image."""
        return self.__emoji


def dancing_emojis(emoji1: Image, emoji2: Image, width: int, height: int, n: int, frames: int = 8) -> Image_Sequence:
    seq = Image_Sequence()
    
    emojis:list[Emoji] = []

    for _ in range(n):
        ran_x = random.randrange(0, width)
        ran_y = random.randrange(0, height)

        emoji = random.choice([emoji1, emoji2])

        emojis.append(Emoji(ran_x, ran_y, emoji))

    for _ in range(frames):
        img = Image_New(width, height)

        for i in range(len(emojis)):
            # translate coordinates randomly based on the MOVEMENT constant over the x and y axis (seperately)
            emojis[i].x = min(max(0, emojis[i].x + random.randint(*MOVEMENT)), width - emoji.get_width())
            emojis[i].y = min(max(0, emojis[i].y + random.randint(*MOVEMENT)), height - emoji.get_height())

            emoji = emojis[i].get_emoji()

            for row in range(emojis[i].y, emoji.get_height() + emojis[i].y):
                for col in range(emojis[i].x, emoji.get_width() + emojis[i].x):
                    pix = emoji.get_pixel(col - emojis[i].x, row - emojis[i].y)

                    if pix != WHITE:
                        img.set_pixel(col, row, pix)

        seq.add_image(img)

    return seq

if __name__ == "__main__":
    emoji1 = Image_File("data/images/smiley.png")
    emoji2 = Image_File("data/images/nauseated.png")

    ems = dancing_emojis(emoji1, emoji2, 600, 400, 80, 100)
    ems.play(15)
