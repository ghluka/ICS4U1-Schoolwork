import os
import sys
from typing import Self

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

import utils.linked_list


class Linked_List(utils.linked_list.Linked_List):
    def get_largest(self) -> object:
        return NotImplemented

    def slice(self, left_index: int, right_index: int) -> Self:
        return NotImplemented

    def left_rotate(self, size: int) -> None:
        return NotImplemented

    def right_rotate(self, size: int) -> None:
        return NotImplemented

if __name__ == "__main__":
    pass
