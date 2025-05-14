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
    test = BSTree()
    test.insert(8)
    test.insert(3)
    test.insert(1)
    test.insert(6)
    test.insert(4)
    test.insert(7)
    test.insert(10)
    test.insert(14)
    test.insert(13)
    test.print_tree()

    print("=-- index() test --=")
    print("Index of 0:", test.index(0)) # -1
    print("Index of 0:", test.index(6)) # 3

    print("=-- average_depth() test --=")
    print(test.average_depth()) # 2.75

    print("=-- ordered_list() test --=")
    print(test.ordered_list()) # [1, 3, 4, 6, 7, 8, 10, 13, 14]

    print("=-- values_at_depth() test --=")
    print("Values at depth 2:", test.values_at_depth(2)) # [1, 6, 14]

    print("=-- longest_path() test --=")
    print(test.longest_path()) # [8,3,6,4], [8,3,6,7], [8,10,14,13]

    print("=-- optimize() test --=")
    test.optimize()
    test.print_tree()
