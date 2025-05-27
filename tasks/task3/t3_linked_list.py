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

    def get_tail(self):
        '''
        Accessor for the value at the end of this linked list.
        '''
        return self.__tail

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

    def remove(self, value: object) -> None:
        '''
        Removes the first occurrence of the specified object from the
        Linked_List, if present.
        '''
        if self.__head == None:
            #empty list case
            self.__tail = None
            return

        elif self.__head.get_data() == value:
            #first item case, where head of list needs updating
            self.__head = self.__head.get_next()
            if self.__head == None:
                self.__tail = None

        else:
            #Trail a 2nd reference to simplify deletion
            previous = self.__head
            current = self.__head.get_next()
            while current != None and current.get_data() != value:
                previous = current
                current = current.get_next()
            if current == None: #item doesnt exist
                return
            else:
                previous.set_next(current.get_next())
                if previous.get_next() == None:
                    self.__tail = previous

    def insert_at(self, index: int, value: object) -> None:
        '''
        Inserts the given value at the given index, shifting all all
        other index values up by one.  For example, lst.insert_at(3, 99)
        would insert the data value 99 at index 3.
        '''
        #handle the head insert separately
        if index == 0:
            self.insert(value)
        else:
            #traverse to node *before* where the insert should happen
            current_i = 1
            current = self.__head
        
            #traverse to the desired index (or off end of list)
            while current != None and current_i != index:
                current = current.get_next()
                current_i += 1
            
            #if the index was actually found (we didnt go off end of list)
            #then insert here
            if current != None:
                new_node = List_Node(value, current.get_next())
                current.set_next(new_node)
                if new_node.get_next() == None:
                    self.__tail = current

            #else: ignore the insert... its an invalid index

    def reverse(self) -> None:
        '''
        Reverses the Linked_List so that it contains all the same data values,
        but in reversed order.  This mutates the linked list.
        '''
        tail = self.__head
        super().reverse()
        self.__tail = tail
    
    # Functions
    def get_largest(self) -> object|None:
        """Returns the largest data value in the linked list.
        If the list is empty, it returns None.
        """
        return self.__get_largest_helper(self.__head)

    def __get_largest_helper(self, node: List_Node) -> object|None:
        """Helper function for get_largest"""
        if node == None:
            return None
        elif node.get_next() == None:
            return node.get_data()
        next_data = self.__get_largest_helper(node.get_next())
        return max(node.get_data(), next_data)

    def slice(self, left_index: int, right_index: int) -> Self:
        """Returns a new Linked_List containing copies of all the data elements
        from left_index up to but not including right_index.

        The ordering isn't changed and if the right_index is greater than the
        left_index, the slice will be empty.
        """
        sliced = Linked_List()

        if right_index < left_index:
            return sliced
        
        n = 0
        current = self.__head

        while current.get_next() != None or n < right_index:
            if n >= left_index:
                sliced.insert_at_end(current.get_data())
            n += 1
            current = current.get_next()
        
        return sliced

    def left_rotate(self, size: int) -> None:
        """Moves the first `size` items to the end"""
        if size == 0:
            return

        head = self.__head

        self.__head = head.get_next()
        self.__tail.set_next(head)
        self.__tail = head
        head.set_next(None)

        self.left_rotate(size - 1)

    def right_rotate(self, size: int) -> None:
        n = 0
        stop = self.size() - size
        current = self.__head

        while n < stop:
            self.__tail.set_next(current)
            self.__tail = current

            n += 1
            current = current.get_next()

        self.__head = current
        self.__tail.set_next(None)

if __name__ == "__main__":
    list_1 = Linked_List()
    list_2 = Linked_List()
    list_3 = Linked_List()
    for i in [1, 2, 3, 4, 5]:
        list_1.insert_at_end(i)
        list_2.insert_at_end(i)
        list_3.insert_at_end(i)
    print(list_1)

    print("=-- get_largest() test --=")
    print(list_1.get_largest()) # 5

    print("=-- slice() test --=")
    print(list_1.slice(1, 4)) # |-[2]->[3]->[4]->x

    print("=-- left_rotate() test --=")
    list_2.left_rotate(1)
    print("Size 1 rotation:", list_2) # |-[2]->[3]->[4]->[5]->[1]->x
    list_2.left_rotate(2)
    print("Size 3 rotation:", list_2) # |-[4]->[5]->[1]->[2]->[3]->x

    print("=-- right_rotate() test --=")
    list_3.right_rotate(1)
    print("Size 1 rotation:", list_3) # |-[5]->[1]->[2]->[3]->[4]->x
    list_3.right_rotate(2)
    print("Size 3 rotation:", list_3) # |-[3]->[4]->[5]->[1]->[2]->x
