import os
import sys
from typing import Self

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

import utils.linked_list
from utils.linked_list import List_Node


class Linked_List(utils.linked_list.Linked_List):
    # Tail implementation
    def __init__(self):
        super().__init__()
        self.__tail = None

    def insert(self, value: object) -> None:
        '''
        Inserts the given value at the front of this linked list.
        '''
        self.__head = List_Node(value, self.__head)
        if self.__head.get_next() == None:
            self.__tail = self.__head

    def insert_at_end(self, value: object) -> None:
        '''
        Inserts the given value at the end of this linked list.
        '''
        # wrap the new value in a Node
        new_node = List_Node(value, None)  # next is None since it is the last

        # we need to handle inserting the FIRST item in an empty list
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node

        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def extend(self, other_list: Self) -> None:
        '''
        Extends this linked list by adding the other_list to the end.
        '''
        self.__tail.set_next(other_list.__head)
        self.__tail = other_list.__tail

    def reverse(self) -> None:
        '''
        Reverses the Linked_List so that it contains all the same data values,
        but in reversed order.  This mutates the linked list.
        '''
        tail = self.__head
        super().reverse()
        self.__tail = tail
    
    # Functions
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
