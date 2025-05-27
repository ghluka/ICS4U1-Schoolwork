import os
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

import utils.bst
from utils.bst import BSTNode


class BSTree(utils.bst.BSTree):
    def index(self, value: object) -> int:
        return self.__index_helper(self.__root, 0, value)
    
    def __index_helper(self, node:BSTNode|None, counter:int, value:object) -> BSTNode|None:
        """Helper function for index"""
        if not node:
            return -1
        elif node.get_data() == value:
            return counter + self.__size_helper(node.get_left())
        elif node.get_data() < value:
            counter += self.__size_helper(node.get_left()) + 1
            return self.__index_helper(node.get_right(), counter, value)
        else:
            return self.__index_helper(node.get_left(), counter, value)

    def average_depth(self) -> float:
        return self.__sum_depth(self.__root, 0)/self.num_leaves()

    def __sum_depth(self, node:BSTNode|None, depth:int) -> int:
        """Helper function for average_depth"""
        if not node:
            return 0
        elif node.get_left() == None and node.get_right() == None:
            return depth
        return self.__sum_depth(node.get_left(), depth + 1) +\
            self.__sum_depth(node.get_right(), depth + 1)

    def ordered_list(self) -> list:
        return self.__ordered_list_helper(self.__root)

    def __ordered_list_helper(self, node: BSTNode|None) -> list:
        """Helper function for ordered_list"""
        if not node:
            return []
        return [
            *self.__ordered_list_helper(node.get_left()),
            node.get_data(),
            *self.__ordered_list_helper(node.get_right())
        ]

    def optimize(self) -> None:
        ordered = self.ordered_list()
        self.__root = None
        self.__optimize_helper(ordered)
    
    def __optimize_helper(self, vals: list) -> None:
        """Helper function for optimize"""
        if len(vals) == 0:
            return
        else:
            mid = len(vals)//2
            self.insert(vals[mid])
            self.__optimize_helper(vals[:mid])
            self.__optimize_helper(vals[mid+1:])

    def values_at_depth(self, depth: int) -> list:
        return self.__values_at_depth_helper(self.__root, 0, depth)

    def __values_at_depth_helper(self, node: BSTNode, current_depth: int, depth: int) -> list:
        """Helper function for values_at_depth"""
        if not node:
            return []
        elif current_depth == depth:
            return [node.get_data()]
        return [
            *self.__values_at_depth_helper(node.get_left(), current_depth+1, depth),
            *self.__values_at_depth_helper(node.get_right(), current_depth+1, depth),
        ]

    def longest_path(self) -> list:
        return self.__longest_path_helper(self.__root)

    def __longest_path_helper(self, node: BSTNode) -> list:
        """Helper function for longest_path"""
        if not node:
            return []
        left = self.__longest_path_helper(node.get_left())
        right = self.__longest_path_helper(node.get_right())

        return [node.get_data(), *max(left, right, key=len)]

if __name__ == "__main__":
    test = BSTree()
    for i in [8, 3, 1, 6, 4, 7, 10, 14, 13]:
        test.insert(i)
    test.print_tree()

    print("=-- index() test --=")
    print("Index of 0:", test.index(0)) # -1
    print("Index of 6:", test.index(6)) # 3

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
