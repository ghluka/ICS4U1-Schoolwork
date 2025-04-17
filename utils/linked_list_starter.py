#LINKED LISTS
 
class List_Node(object):
    
    def __init__(self, data, next_node):
        self.__data = data      #the data contained in this node
        self.__next = next_node #reference to the next List_Node
    
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
        self.__head = None  #a List_Node, the first one in the list
        

    def insert(self, value):
        '''
        Inserts the given value at the front of this linked list.
        '''
        self.__head = List_Node(value, self.__head)


    def is_empty(self):
        '''
        Return True if this list is empty, or False otherwise
        '''
        return self.__head == None
        



    def print(self):
        '''
        Prints each vale in the linked list, one per line.
        '''
        #starting at the first (HEAD)
        current = self.__head  # an ALIAS
        #while I have not looked at all items:
        while current != None:
            #print this item
            print(current.get_data())
            #and go to the next
            current = current.get_next()
            


    def __str__(self):
        '''
        Returns a string representation of this Linked_List
        '''
        pass

    
    def size(self):
        '''
        Returns the number of items in this Linked_List.
        '''
        count = 0
        #starting at the first (HEAD)
        current = self.__head  # an ALIAS
        #while I have not looked at all items:
        while current != None:
            #count this item
            count += 1
            #and go to the next
            current = current.get_next()
        return count
            


    def contains(self, value):
        '''
        Returns True if this Linked_List contains the given object, or False otherwise.
        '''
        pass


    def insert_at_end(self, value):
        '''
        Inserts the given value at the end of this linked list.
        '''
        pass


    def extend(self, other_list):
        '''
        Extends this linked list by adding the other_list to the end.
        '''
        pass


    def remove(self, value):
        '''
        Removes the specified object from the Linked_List, if present.
        '''
        #.... this one will require signifiantly more effort...




if __name__ == "__main__":
    lst = Linked_List()
    lst.print()
    print(lst.size())
    print(lst.is_empty())
    print('-'*40)
    #print(lst.contains(0))
    
    for num in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        lst.insert(num)
    lst.print()
    print(lst.size())
    #print(lst.is_empty())
    #print(lst.contains(0))
    #print(lst.contains(2))
    #print(lst.contains(11))
    #print(lst.contains(23))
    