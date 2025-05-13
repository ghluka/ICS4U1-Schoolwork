from typing import Self


class List_Node(object):
    
    def __init__(self, data, next_node):
        self.__data = data      # the data contained in this node
        self.__next = next_node # reference to the next List_Node
    
    def get_next(self):
        return self.__next
    
    def get_data(self):
        return self.__data

    def set_next(self, node):
        self.__next = node
    
    def set_data(self, value):
        self.__data = value

    def __str__(self):
        return f"[{self.__data}]->"



class Linked_List(object):
    
    def __init__(self):        
        '''
        Construct an empty linked list.
        '''
        self.__head = None  # a List_Node, the first one in the list
        

    def insert(self, value: object) -> None:
        '''
        Inserts the given value at the front of this linked list.
        '''
        self.__head = List_Node(value, self.__head)


    def is_empty(self) -> bool:
        '''
        Return True if this list is empty, or False otherwise
        '''
        return self.__head == None


    def __str__(self) -> str:
        '''
        Returns a string representation of this Linked_List
        '''
        list_str = "|-"
        # starting at the first (HEAD)...
        current = self.__head  # an ALIAS

        # while I have not looked at all items...
        while current != None:
            # add this node to the string
            list_str += f"{current}"
            # and go to the next
            current = current.get_next()

        list_str += "x"  # placed to indicate 'None'
        return list_str

    
    def size(self) -> int:
        '''
        Returns the number of items in this Linked_List.
        '''
        count = 0
        # starting at the first...
        current = self.__head
        
        # while I have not looked at all items...
        while current != None:
            # count this item
            count += 1
            # and go to the next
            current = current.get_next()
        return count


    def contains(self, value: object) -> bool:
        '''
        Returns True if this Linked_List contains the given object, or False otherwise.
        '''
        # starting at the first...
        current = self.__head

        seen_it = False # keep track if we have seen the item or not

        # while I have not looked at all items or we have found it...
        while current != None and not seen_it:
            # if we found it, update the status
            if current.get_data() == value:
                seen_it = True

            # and go to the next
            current = current.get_next()
        return seen_it


    def insert_at_end(self, value: object) -> None:
        '''
        Inserts the given value at the end of this linked list.
        '''
        # wrap the new value in a Node
        new_node = List_Node(value, None)  # next is None since it is the last
                
        # we need to handle inserting the FIRST item in an empty list
        # as a special case, sice it would need to update the __head property.
        if self.__head == None:
            self.__head = new_node

        else:  # otherwise, loop to the end of the list

            # starting at the first...
            current = self.__head
    
            # while I am not at the LAST item in the list...
            while current.get_next() != None:
                # go to the next
                current = current.get_next()
            
            # now, attach this new last item to the new Node
            current.set_next(new_node)



    def extend(self, other_list: Self) -> None:
        '''
        Extends this linked list by adding the other_list to the end.
        '''
        # starting at the first item in myself
        current = self.__head
        
        # while I am not at the LAST item in me...
        while current.get_next() != None:
            # go to the next
            current = current.get_next()
        

        # Now, one by one make new Nodes with copies of the data
        # in the 'other' list and add them at the end of me.
        # This will require a separate 'current'
        # reference for each list.

        # starting at the first Node in the other list...
        current_other = other_list.__head

        # while we haven't looked at all values in the other list...
        while current_other != None:
            # make a new Node that copies the data
            new_node = List_Node(current_other.get_data(), None)
           
            # link up the end of the first list to this new node
            current.set_next(new_node)
            
            # now move our 'end of first list' reference new the new last node...
            current = new_node
            
            #...and go on to the next value in the other list
            current_other = current_other.get_next()


    def remove(self, value: object) -> None:
        '''
        Removes the first occurrence of the specified object from the
        Linked_List, if present.
        '''
        if self.__head == None:
            #empty list case
            return

        elif self.__head.get_data() == value:
            #first item case, where head of list needs updating
            self.__head = self.__head.get_next()

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


    def get_value_at(self, index: int) -> object:
        '''
        Returns the data value at the given index in the list
        (with 0 being the first index).
        '''
        # starting at the first item...
        current = self.__head
        current_pos = 0
        
        # while I haven't reached the index or gone off the end of the list
        while current != None and current_pos != index:
            # go to the next and update the current position
            current = current.get_next()
            current_pos += 1
            
        # now, check if we made it to the index or not
        # and return the value (or None if it wasn't found)
        if current != None:
            return current.get_data()
        else:
            return None
    
    
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

            #else: ignore the insert... its an invalid index

 
    def reverse(self) -> None:
        '''
        Reverses the Linked_List so that it contains all the same data values,
        but in reversed order.  This mutates the linked list.
        '''
        rev = Linked_List()  #the new reversed list

        #traverse through list in-order, and insert each at head of new list
        curr = self.__head
        while curr != None:
            rev.insert(curr.get_data())
            curr = curr.get_next()
        
        # now make the head refer to the head of this new list instead
        self.__head = rev.__head        

    
    #===========================================================================
    #===========================================================================
    #===========================================================================
    #===========================================================================
    
    #= ADDITIONAL METHODS ======================================================

    def get_largest(self) -> object:
        return NotImplemented
    
    
    def slice(self, left_index: int, right_index: int) -> Self:
        return NotImplemented

   
    def left_rotate(self, size: int) -> None:
        return NotImplemented

    
    def right_rotate(self, size: int) -> None:
        return NotImplemented
    