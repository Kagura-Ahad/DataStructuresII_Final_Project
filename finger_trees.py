from typing import List, Union, TypeVar, Optional, Generic, Tuple

T = TypeVar('T')

class Affix:
    
    # Constructor for initializing the object
    def __init__(self, *args: T) -> None:
        self.elements = args

    # Returns a string representation of the object
    def __repr__(self) -> str:
        return f'({", ".join(map(str, self.elements))})'
    
    # Overloading the bitwise or operator to concatenate two Affix objects
    def __or__(self, other: 'Affix[T]') -> 'Affix[T]':
        return Affix(*self.elements, *other.elements)
    
    # Returns a boolean indicating whether the Affix is empty or not
    def isEmpty(self) -> bool:
        return not(self.elements)


class View(Generic[T]):

    # Constructor for initializing the object
    def __init__(self, head: T, tail: Optional['FingerTree[T]']) -> None:
        self.head = head
        self.tail = tail


class FingerTree:
    
    # Constructor method
    def __init__(self, prefix: Affix, deeper: Union['FingerTree[T]', None], suffix: Affix) -> None:
        self.prefix = prefix
        self.deeper = deeper
        self.suffix = suffix
    
    # Returns the total number of elements in the FingerTree
    def __len__(self) -> int:
        return sum([len(self.prefix.elements), len(self.suffix.elements), self.deeper.__len__() if self.deeper is not None else 0])

    # Returns a string representation of the FingerTree
    def __repr__(self) -> str:
        return f'{{prefix = {repr(self.prefix)}, deeper = {repr(self.deeper)}, suffix = {repr(self.suffix)}}}'

    # Returns a human-readable string representation of the FingerTree
    def __str__(self) -> str:
        if self.suffix.isEmpty() and self.prefix.isEmpty():
            return f'None'
        return f'{{prefix = {self.prefix}, deeper = {self.deeper.__str__()}, suffix = {self.suffix}}}'

    # Static method to create an empty FingerTree
    @staticmethod
    def empty() -> 'FingerTree[T]':
        return FingerTree(Affix(), None, Affix())

    # Static method to create a FingerTree with a single element
    @staticmethod
    def single(x: T) -> 'FingerTree[T]':
        return FingerTree(Affix(x), None, Affix())
    
    def prepend(self, x: T) -> None:
        # Check if prefix is full
        if len(self.prefix.elements) == 4: 
            # create a node out of the last three elements of the prefix
            node = (self.prefix.elements[3], self.prefix.elements[2], self.prefix.elements[1]) 
            # If there is no deeper tree, create one with the new node's elements
            if self.deeper is None: 
                self.deeper = FingerTree(Affix(), None, Affix())
                for i in node:
                    self.deeper.prefix = Affix(i) | self.deeper.prefix  
            else:
                # If there is a deeper tree, prepend the new node's elements to it
                for i in node: 
                    self.deeper.prepend(i) 
            # set the new prefix with x added to the beginning and the last element of the old prefix
            self.prefix = Affix(x, self.prefix.elements[0]) 
        else:
            # If the current prefix is not full, add the new element to it
            self.prefix = Affix(x) | self.prefix 


    def append(self, x: T) -> None:
        # Check if the current suffix is full (has 4 elements)
        if len(self.suffix.elements) == 4:
            # Create a new node with the last three elements of the current suffix
            node = (self.suffix.elements[0], self.suffix.elements[1], self.suffix.elements[2])
            if self.deeper is None:
                # If there is no deeper tree, create one with the new node's elements
                self.deeper = FingerTree(Affix(), None, Affix())
                for i in node:
                    self.deeper.suffix = self.deeper.suffix | Affix(i)
            else:
                # If there is a deeper tree, append the new node's elements to it
                for i in node:
                    self.deeper.append(i)
            # Set the new suffix to be x and the first element of the old suffix
            self.suffix = Affix(self.suffix.elements[3], x)
        else:
            # If the current suffix is not full, add the new element to it
            self.suffix = self.suffix | Affix(x)



    def viewl(self) -> View[T]:
        # Check if the prefix is empty.
        if self.prefix.elements == []:
            return View(None, None)

        # Check if the prefix has only one element and there is no deeper tree.
        if len(self.prefix.elements) == 1 and self.deeper is None:
            return View(self.prefix.elements[0], None)

        # Check if the prefix has only one element and there is a deeper tree.
        if len(self.prefix.elements) == 1:
            x = self.prefix.elements[0]
            # Recursively call viewl() on the deeper tree.
            deeper_rest = self.deeper.viewl()
            if deeper_rest.tail is None:
                # If the deeper tree's tail is None and suffix is empty, return the element x with no tail.
                if self.suffix.elements == []:
                    return View(x, None)
                # If suffix is not empty, return the element x with the first element of suffix as the tail.
                return View(x, FingerTree.single(self.suffix.elements[0]))
            # If the deeper tree's tail is not None, get the head node and the rest of the tree.
            node, rest = deeper_rest.head, deeper_rest.tail
            # Return the element x with the deeper tree's head node as the prefix and the rest of the tree as the deeper tree.
            return View(x, FingerTree(Affix(*node.elements), rest, self.suffix))

        # If the prefix has more than one element, get the first element as x and the rest as rest.
        x, *rest = self.prefix.elements
        # Return the element x with the rest of the prefix as the prefix and the current deeper tree and suffix as is.
        return View(x, FingerTree(Affix(*rest), self.deeper, self.suffix))


    def viewr(self) -> View[T]:
        # If the suffix is empty, return an empty view
        if self.suffix.elements == []:
            return View(None, None)

        # If there is only one element in the suffix and there are no deeper nodes, 
        # return a view containing that element
        if len(self.suffix.elements) == 1 and self.deeper is None:
            return View(self.suffix.elements[0], None)

        # If there is only one element in the suffix and there are deeper nodes, 
        # return a view containing that element and the tail of the deeper tree
        if len(self.suffix.elements) == 1:
            x = self.suffix.elements[0]
            deeper_rest = self.deeper.viewr()
            
            # If the tail of the deeper tree is None, return a view containing the 
            # suffix element and the last element in the prefix (if it exists)
            if deeper_rest.tail is None:
                if self.prefix.elements == []:
                    return View(x, None)
                return View(x, FingerTree.single(self.prefix.elements[-1]))
            
            # Otherwise, extract the head and tail of the deeper tree and construct
            # a new FingerTree with the suffix element and the head of the deeper tree
            node, rest = deeper_rest.tail, deeper_rest.head
            return View(x, FingerTree(self.prefix, rest, Affix(*node.elements)))

        # If there are multiple elements in the suffix, extract the last element 
        # and construct a new FingerTree with the remaining elements in the suffix
        *rest, x = self.suffix.elements
        return View(x, FingerTree(self.prefix, self.deeper, Affix(*rest)))

    
    def treeHead(self):
        view = self.viewl()
        if view.tail is None:
            raise Exception("no elements in tree")
        return view.head

    def treeTail(self):
        view = self.viewl()
        if view.tail is None:
            raise Exception("no elements in tree")
        return view.tail

    def treeLast(self):
        view = self.viewr()
        if view.tail is None:
            raise Exception("no elements in tree")
        return view.head

    def treeInit(self):
        view = self.viewr()
        if view.tail is None:
            raise Exception("no elements in tree")
        return view.tail
    
    def toList(self) -> List:
        result = list(self.prefix.elements)
        if self.deeper is not None:
            result += self.deeper.toList()
        result += list(self.suffix.elements)
        return result

    def lookup(self, value: T) -> Optional[int]:
        # Check if the value is in the prefix
        for i, x in enumerate(self.prefix.elements):
            if x == value:
                return i

        # Check if the value is in the suffix
        for i, x in enumerate(self.suffix.elements):
            if x == value:
                return len(self.prefix.elements) + self.deeper.__len__() + i

        # If there is a deeper tree, recursively call lookup() on it
        if self.deeper is not None:
            result = self.deeper.lookup(value)
            if result is not None:
                return result + len(self.prefix.elements)

        # If the value is not found, return None
        return None
    
    def split(self, i: int) -> Tuple['FingerTree[T]', 'FingerTree[T]']:
        # If i is non-positive, return an empty FingerTree and None as the separator.
        if i <= 0:
            return FingerTree.empty(), self
        
        # If i is greater than the length of the FingerTree, return self and None as the separator.
        elif i >= len(self):
            return self, FingerTree.empty()
        
        # If i is in the prefix of the FingerTree
        elif i < len(self.prefix.elements):
            newTreeLeft = FingerTree(Affix(), None, Affix())
            newTreeRight = FingerTree(Affix(), self.deeper, self.suffix)
            for i in self.prefix.elements[:i]:
                newTreeLeft.prepend(i)
            for i in self.prefix.elements[i:]:
                newTreeRight.prepend(i)
            return newTreeLeft, newTreeRight

        # If i is in the suffix of the FingerTree 
        elif i > len(self.prefix.elements) + len(self.suffix.elements):
            newTreeLeft = FingerTree(self.prefix, self.deeper, Affix())
            newTreeRight = FingerTree(Affix(), None, Affix())
            index = len(self) - len(self.suffix.elements)
            for i in self.suffix.elements[:i-index]:
                newTreeLeft.append(i)
            for i in self.suffix.elements[i-index-1:]:
                newTreeRight.append(i)
            return newTreeLeft, newTreeRight
        
        else:
            # If i is in the deeper tree, recursively split the deeper tree.
            left_deeper, right_deeper = self.deeper.split(i - len(self.prefix.elements))
            if left_deeper is FingerTree.empty():
                left = self.prefix
            else:
                for i in self.prefix.elements:
                    left_deeper.prepend(i)
                left = left_deeper
            if right_deeper is FingerTree.empty():
                right = self.suffix
            else:
                for i in self.suffix.elements:
                    right_deeper.append(i)
                right = right_deeper
            return left, right




def fromList(lst: List[T]) -> 'FingerTree[T]':
    tree = FingerTree.empty()
    for x in lst:
        tree.append(x)
    return tree

#function_tests
# layer3 = FingerTree.empty()
# layer2 = FingerTree(Affix(1, 2, 3), layer3, Affix(4, 5, 6))
# layer1 = FingerTree(Affix(7, 8), layer2, Affix(11, 10))
# ft = layer1

# print(ft)

# print(ft.split(3))  