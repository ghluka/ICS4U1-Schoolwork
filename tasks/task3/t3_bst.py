import os
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

import utils.bst


class BSTree(utils.bst.BSTree):
    def index(self, value: object) -> int:
        return NotImplemented

    def average_depth(self) -> float:
        return NotImplemented

    def ordered_list(self) -> list:
        return NotImplemented

    def optimize(self) -> None:
        return NotImplemented

    def values_at_depth(self, depth: int) -> list:
        return NotImplemented

    def longest_path(self) -> list:
        return NotImplemented

if __name__ == "__main__":
    pass
