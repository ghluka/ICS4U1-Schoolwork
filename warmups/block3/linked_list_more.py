import os
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.linked_list_starter import Linked_List, List_Node


class Linked_List2(Linked_List):

    def __str__(self) -> str:
        '''
        Returns a string representation of this Linked_List
        '''
        chain = "|-"
        current:List_Node = self._Linked_List__head

        while current != None:
            chain += f"[{current.get_data()}]->"

            current = current.get_next()
        return chain.rstrip(">").rstrip("-")

    def contains(self, value:object) -> bool:
        '''
        Returns True if this Linked_List contains the given object, or False otherwise.
        '''
        current:List_Node = self._Linked_List__head

        while current != None:
            if current.get_data() == value:
                return True

            current = current.get_next()
        return False

    def insert_at_end(self, value:object) -> None:
        '''
        Inserts the given value at the end of this linked list.
        '''
        current:List_Node = self._Linked_List__head

        if not current:
            super().insert(value)
            return

        while current.get_next() != None:
            current = current.get_next()

        last = List_Node(value, None)
        current.set_next(last)

    def extend(self, other_list:Linked_List) -> None:
        '''
        Extends this linked list by adding the other_list to the end.
        '''
        current:List_Node = self._Linked_List__head
        other_head:List_Node = other_list._Linked_List__head

        if not current:
            self._Linked_List__head = other_head
            return

        while current.get_next() != None:
            current = current.get_next()

        current.set_next(other_list._Linked_List__head)

if __name__ == "__main__":
    lst = Linked_List2()
    lst2 = Linked_List2()
    lst3 = Linked_List2()

    print("insert_at_end() test:")
    for num in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        lst.insert(num)
        lst2.insert_at_end(num)
    print('-'*40)

    print("__str__() test:")
    print(">>", lst)
    print(">>", lst2)
    print('-'*40)

    print("extend() test:")
    lst.extend(lst2)
    print(">>", lst)
    print('-'*40)

    print("contains() test:")
    print(">>", lst.contains(0)) # False
    print(">>", lst2.contains(2)) # True
    print(">>", lst3.contains(11)) # False
    print(">>", lst.contains(23)) # True
    print('-'*40)

    #lst.extend(lst)
    #print(lst)
