from typing import Optional


class BSTNode(object):
    
    def __init__(self, value):
        self.__data = value
        self.__left = None
        self.__right = None

    def get_data(self):
        return self.__data
    def set_data(self, data):
        self.__data = data
    def get_left(self):
        return self.__left
    def set_left(self, node):
        self.__left = node
    def get_right(self):
        return self.__right
    def set_right(self, node):
        self.__right = node


class BSTree(object):
    
    def __init__(self) -> None:
        '''Construct an empty binary search tree.'''        
        self.__root:Optional[BSTNode] = None
        
    def insert(self, val: object) -> None:
        '''
        Insert the value into tree.
        '''
        new_node = BSTNode(val)
        temp:BSTNode = self.__root
        
        #first insert
        if temp == None:
            self.__root = new_node

        #'standard' case
        else:
            inserted = False
            while not inserted:
                if val < temp.get_data():
                    #insert the new node if we have reached the 'leaves'
                    if temp.get_left() == None:
                        temp.set_left(new_node)
                        inserted = True
                    else:
                        temp = temp.get_left()
                else:
                    if temp.get_right() == None:
                        temp.set_right(new_node)
                        inserted = True
                    else:
                        temp = temp.get_right()


    def in_order_traversal(self) -> None:
        '''
        Print an in-order traversal of the tree.
        '''
        self.__in_order_helper(self.__root)
    def __in_order_helper(self, subroot: Optional[BSTNode]) -> None:
        if subroot != None:
            self.__in_order_helper(subroot.get_left())
            print(subroot.get_data())
            self.__in_order_helper(subroot.get_right())


    def pre_order_traversal(self) -> None:
        '''
        Print a pre-order traversal of the tree.
        '''
        self.__pre_order_helper(self.__root)
    def __pre_order_helper(self, subroot: Optional[BSTNode]) -> None:
        if subroot != None:
            print(subroot.get_data())
            self.__pre_order_helper(subroot.get_left())
            self.__pre_order_helper(subroot.get_right())


    def post_order_traversal(self) -> None:
        '''
        Print a post-order traversal of the tree.
        '''
        self.__post_order_helper(self.__root)
    def __post_order_helper(self, subroot: Optional[BSTNode]) -> None:
        if subroot != None:
            self.__post_order_helper(subroot.get_left())
            self.__post_order_helper(subroot.get_right())
            print(subroot.get_data())


    def print_tree(self) -> None:
        '''
        Prints the tree in a 'sideways' representation, with spaces to show depth.
        '''        
        #Use a recursive private 'helper' method
        self.__print_helper(self.__root, 0)
    
    def __print_helper(self, node: Optional[BSTNode], depth: int) -> None:
        '''A helper method for the print_tree() method.
        Takes the 'root' of a sub-part of the tree (just a BSTNode)
        and the currentent 'depth' of this sub-root in the tree (for formatting).
        Base case: sub-root is None, so we're done that branch
        Recursive case: re-call this helper method on each 'side' of this subroot,
                        printing itself in-between.  Add 1 to depth for each call.
        '''
        
        if node != None: #if I haven't gone off end of a branch
            #print right subtree, print me, print left subtree
            self.__print_helper(node.get_right(), depth+1)
            indent = "     "*depth
            print(f"{indent}[{node.get_data()}]")
            self.__print_helper(node.get_left(), depth+1)
        
    

    '''=== METHODS FOR YOU TO WORK ON! ================================='''
    def maximum(self) -> object:
        '''
        Return the 'maximum' value in the tree.
        This is the value farthest to the 'right'.
        '''
        #handle the empty tree case
        if self.__root == None:
            return None

        #start at the root and go as far right as possible
        currentent = self.__root
        
        #as long as there is a node to teh right
        while currentent.get_right() != None:
            #go to the right!
            currentent = currentent.get_right()
            
        #wherever we end up is the maximum!
        return currentent.get_data()



    def minimum(self) -> object:
        '''
        Return the 'minimum' value in the tree.
        This is the value farthest to the 'left'.
        '''
        #start at the root and go as far left as possible
        currentent:BSTNode = self.__root
        #as long as there is a node to the left
        while currentent.get_left() != None:
            #go to the left!
            currentent = currentent.get_left()
            
        #wherever we end up is the minimum!
        return currentent.get_data()
    
    

    def size(self) -> int:
        '''
        Return the number of nodes in this tree.
        '''
        #Dont add instance variables!
        #Look at the way the print method worked, and structure this the same way.
        #Perhaps add a helper method?
        return self.__size_helper(self.__root)
    def __size_helper(self, subroot):
        #Size from any subroot down is size(left) + size(right) + 1 
        if subroot == None:
            #size of None is 0
            return 0
        else:
            left_size = self.__size_helper(subroot.get_left())
            right_size = self.__size_helper(subroot.get_right())
            return left_size + right_size + 1



    def height(self) -> int:
        '''
        Return the depth of the largest 'branch' in this tree.
        '''
        return self.__height_helper(self.__root) - 1
    def __height_helper(self, subroot):
        if subroot == None:
            #size of None is 0
            return 0
        else:
            #height is the larger of the left and right subtree heights
            #plus 1 (because the subroot adds to the hright by 1)
            left_height = self.__height_helper(subroot.get_left())
            right_height = self.__height_helper(subroot.get_right())

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1
            
            #simpler version than if-else:
            #return max(left_height, right_height) + 1
    

    def num_leaves(self) -> int:
        '''
        Return the number of leaves in this tree.
        '''
        return self.__num_leaves_helper(self.__root)
    def __num_leaves_helper(self, subroot):
        if subroot == None:
            #a None subroot has 0 leaves
            #we need to check this case first to avoid NoneType exceptions
            return 0
        elif subroot.get_left() == None and subroot.get_right() == None:
            #a leaf has no left/right children
            return 1
        else:
            #the number of leaves is number in left + number in right
            left_n = self.__num_leaves_helper(subroot.get_left())
            right_n = self.__num_leaves_helper(subroot.get_right())
            return left_n + right_n


    def remove(self, value: object) -> None:
        '''
        Remove the value from the tree, if present.
        '''
        # Using a helper allows us to have the remove() return what this
        # root should now refer to
        self.__root = self.__remove_helper(self.__root, value)
    def __remove_helper(self, subroot: Optional[BSTNode], value: object) -> Optional[BSTNode]:
        #RETURNS the BSTNode that the parent should refer to 
        
        # When the subroot is None, we went off the tree (didnt find it!)
        if subroot == None:
            return None
        
        # A BSTNode exists here.  Should I look left or right for the value?
        elif value < subroot.get_data():
            # set my left to whatever the delete tells me to when
            # I delete the value from my left subtree 
            subroot.set_left(self.__remove_helper(subroot.get_left(), value))
            return subroot #tell whoever called me to link up to me

        elif value > subroot.get_data():
            # set my right to whatever the delete tells me to when
            # I delete the value from my right subtree 
            subroot.set_right(self.__remove_helper(subroot.get_right(), value))
            return subroot #tell whoever called me to link up to me        
        
        else:  #I'm AT the node i want to delete
                
            # subroot has 0 children, so tell my parent to refer to None
            if subroot.get_left() == None and subroot.get_right() == None:
                return None        
    
            # subroot has 1 child
            elif subroot.get_left() == None:
                # means the RIGHT ISNT None, so my parent should refer to it
                return subroot.get_right()
            elif subroot.get_right() == None:
                # means the LEFT ISNT None, so my parent should refer to it
                return subroot.get_left()        

            else:
                # subroot has 2 children
                # find successor, copy data, call delete from right
                succ = subroot.get_right()
                while succ != None:
                    succ = succ.get_left()
                
                #copy the data
                subroot.set_data(succ.get_data())
                
                #delete that copied value from right subtree
                subroot.set_right(self.__remove_helper(subroot.get_right(), succ.get_data()))
                return subroot


    def remove2(self, value):
        '''
        Remove the value from the tree, if present.
        '''
        # This is an ITERATIVE version, which some of you may be more
        # comfortable with
        
        # Like with Linked_List remove, this will keep a 'previous'
        # reference, which is really the parent node of current
        parent = None
        current = self.__root
   
        # Traverse to the node to delete (or off the tree of not found)
        while current != None and current.get_data() != value:
            parent = current
            if value < current.get_data():
                current = current.get_left()
            else:
                current = current.get_right()
   
        if current != None:
            #  then we found the value, so proceed with a removal
   
            # Case 1 and 2: Node is a leaf with 0 children, or 1 child
            if current.get_left() == None or current.get_right() == None:
                # First determine what the 'child' is

                if current.get_left() != None:
                    # If the child is to the left:
                    child = current.get_left()
                elif current.get_right() != None:
                     # If the child is to the left:
                    child = current.get_right()
                else:
                    # both children are None (this is a leaf):
                    child = None
                    
                    
                # Now, set the parent to point to that child
                if parent == None:
                    # Deleting the root node
                    self.__root = child
                elif parent.get_left() == current:
                    # we went LEFT from the parent, so set the parent's
                    # left to None to delete this leaf
                    parent.set_left(child)
                else:
                    # we went RIGHT from the parent, so set the parent's
                    # right to None to delete this leaf
                    parent.set_right(child)
   
            else:
                # Case 3: Node has two children
                # Find the successor (smallest in the right subtree)
                succ_parent = current
                succ = current.get_right()
                while succ.get_left() != None:
                    succ_parent = succ
                    succ = succ.get_left()
   
                # Replace current's value with successor's value
                current.set_data(succ.get_data())
 
   
                # Delete the successor node, which MUST be either a
                # leaf or only have a right child.  Either way, the
                # parent should now refer to the RIGHT of the successor 
                if succ_parent.get_left() == succ:
                    # if we went left from the parent
                    succ_parent.set_left(succ.get_right())
                else:
                    # if we went right from the parent
                    succ_parent.set_right(succ.get_right())                   


    #===========================================================================
    #===========================================================================
    #===========================================================================
    #===========================================================================
    
    #= ADDITIONAL METHODS ======================================================
    
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

