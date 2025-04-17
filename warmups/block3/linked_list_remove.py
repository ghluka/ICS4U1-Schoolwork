import os
import sys

# fix path to allow utils imports
# note to self: do not submit assignments with this "import" hack, it's just to get utils working
sys.path[0] = os.getcwd()

from utils.linked_list_starter import Linked_List, List_Node


class Linked_List2(Linked_List):

    def remove(self, value:object) -> None:
        '''
        Removes the specified object from the Linked_List, if present.
        '''
        current:List_Node = self._Linked_List__head
        trailer:List_Node = current

        while current != None:
            if current.get_data() == value:
                if current is trailer:
                    self._Linked_List__head = current.get_next()
                else:
                    trailer.set_next(current.get_next())
                break

            trailer = current
            current = current.get_next()

if __name__ == "__main__":
    lst = Linked_List2()

    for num in [2, 5, 4, 7, 3]:
        lst.insert(num)

    lst.remove(4)

    lst.remove(2)

    lst.remove(0)

    lst.remove(3)

    lst.remove(7)
    lst.remove(5)

    lst.remove(5)
