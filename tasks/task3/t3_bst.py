import utils.bst
from utils.bst import BSTNode


class BSTree(utils.bst.BSTree):
    def index(self, value: object) -> int:
        """Returns the index of the given value (indexing from 0) or returns -1
        if the value is not in the tree.
        The index is based on the position of the value in the sorted collection.
        """
        return self.__index_helper(self.__root, 0, value)
    
    def __index_helper(self, node:BSTNode|None, counter:int, value:object) -> int:
        """Helper function for index."""
        # empty tree or attempting to go past a leaf case
        if not node:
            return -1
        elif node.get_data() == value:
            return counter + self.__size_helper(node.get_left())
        elif node.get_data() < value:
            # cut off all the values to the left from the search, and add all
            # indices of values that are smaller than the value being indexed
            counter += self.__size_helper(node.get_left()) + 1
            return self.__index_helper(node.get_right(), counter, value)
        return self.__index_helper(node.get_left(), counter, value)

    def average_depth(self) -> float:
        """Returns the average depth of all the leaf nodes in the tree, where
        depth is the length of the path from the root to that leaf measured
        in edges.
        """
        return self.__sum_depth(self.__root, 0)/self.num_leaves()

    def __sum_depth(self, node:BSTNode|None, depth:int) -> int:
        """Helper function for average_depth."""
        # empty tree or attempting to go past a leaf case
        if not node:
            return 0
        # leaf case
        elif node.get_left() == None and node.get_right() == None:
            return depth
        return self.__sum_depth(node.get_left(), depth + 1) +\
            self.__sum_depth(node.get_right(), depth + 1)

    def ordered_list(self) -> list:
        """Returns all the values from the tree in a Python list, ordered from
        smallest to largest.
        """
        return self.__ordered_list_helper(self.__root)

    def __ordered_list_helper(self, node: BSTNode|None) -> list:
        """Helper function for ordered_list."""
        # empty tree case
        if not node:
            return []

        return [
            *self.__ordered_list_helper(node.get_left()), # the ordered list version of the LEFT subtree from the node
            node.get_data(), # node's data itself
            *self.__ordered_list_helper(node.get_right()) # the ordered list version of the RIGHT subtree from the node
        ]

    def optimize(self) -> None:
        """Re-creates the tree by resetting the root to None and re-inserting
        all the values from the tree into itself in a fashion that would create
        a tree that is as full as possible at each level, except the last.
        """
        # create tree based on ordered list
        ordered = self.ordered_list()
        self.__root = None
        self.__optimize_helper(ordered)
    
    def __optimize_helper(self, vals: list) -> None:
        """Helper function for optimize."""
        # empty list case
        if len(vals) == 0:
            return
        mid = len(vals)//2

        self.insert(vals[mid])
        self.__optimize_helper(vals[:mid])
        self.__optimize_helper(vals[mid+1:])

    def values_at_depth(self, depth: int) -> list:
        """Returns a Python list that contains all the data values that exist in
        the tree at exactly the specified depth.
        """
        return self.__values_at_depth_helper(self.__root, 0, depth)

    def __values_at_depth_helper(self, node: BSTNode|None, current_depth: int, depth: int) -> list:
        """Helper function for values_at_depth."""
        # empty tree case
        if not node:
            return []
        # return current data if at depth
        elif current_depth == depth:
            return [node.get_data()]
        # merge all data yielded from left and right nodes
        return [
            *self.__values_at_depth_helper(node.get_left(), current_depth+1, depth),
            *self.__values_at_depth_helper(node.get_right(), current_depth+1, depth),
        ]

    def longest_path(self) -> list:
        """Returns a Python list that contains all the data values that exist in
        the tree along the path from the root to the deepest leaf.
        """
        return self.__longest_path_helper(self.__root)

    def __longest_path_helper(self, node: BSTNode|None) -> list:
        """Helper function for longest_path."""
        # empty tree or trying to go past leaf case
        if not node:
            return []

        left = self.__longest_path_helper(node.get_left())
        right = self.__longest_path_helper(node.get_right())

        # return current data and greatest of the left or right node
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
