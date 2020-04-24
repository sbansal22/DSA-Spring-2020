"""
Author: Sparsh Bansal
DSA Homework 5

"""

# Importing Python modules
import pytest
from hypothesis import given
import hypothesis.strategies as st
import math

# Defining the Heap Class
class Heap:
    def __init__(self, oglist = []):
        ''' Initialize heap from a (possibly empty) list. '''
        
        # This structure tracks the length and root of the heap
        # Sets the length of the heap
        self.leng = len(oglist)
        
        # Case I - The heap is initialized with a non-empty list
        if self.leng != 0:
            self.heap = self.sorter(oglist)
            self.root = self.heap[0]
        
        # Case II - The heap is initialized with an empty list
        else:
            self.heap = []
            self.root = None

    def length(self):
        ''' Return length of the heap. '''

        return self.leng
        
    def insert(self, value):
        ''' Insert value into the heap. '''

        # Appends the value as a child in the lowest level of 
        # the heap
        self.heap.append(value)
        
        # Updates the length of the heap
        self.leng += 1

        # Sorts the heap to maintain the min-heap structure
        if self.leng > 1:
            self.heap = self.sorter(self.heap)
        
        # Updates the root of the heap
        self.root = self.heap[0]


    def delete_min(self):
        ''' Remove the min (root) from heap. '''

        # Assigns the min to be a child in the lowest level of
        # the heap
        self.heap[0] = self.heap[-1]
        
        # Deletes the min of the heap
        del self.heap[-1]

        # Updates the length of the heap
        self.leng -= 1

        if self.leng >= 1:

            # Sorts the heap in order to maintain the min heap
            # structure
            self.heap = self.sorter(self.heap)

            # Updates the root of the heap
            self.root = self.heap[0]


    def find_min(self):
        ''' Return min value in the heap. '''
        
        return self.heap[0]

    def sorted_list(self):
        ''' Return a sorted list of all heap elements. '''

        # Initializes a buffer list
        temp_list = []

        # Creates a min list based on recursing through the 
        # heap and continously deleting the min
        while len(self.heap) > 0:
            temp_list.append(self.heap[0])
            self.delete_min()
        
        return temp_list

    def sorter(self, oglist):
        ''' Carries out percolations in order to maintain
        the min-heap structure'''

        if self.leng < 1:
            return oglist
        else:
            # Calculates the height of the heap 
            height = math.ceil(math.log2(self.leng)) + 1

        while height > 0:
            # Percolation
            for i in range(self.leng -1, 0, -1):
                chld = i
                prnt = (i-1)//2
                if oglist[chld] < oglist[prnt]:
                    temp = oglist[chld]
                    oglist[chld] = oglist[prnt]
                    oglist[prnt] = temp
            height -= 1 

        return oglist

# Testing the hypothesis function
@given(st.lists(st.integers()))
def test_heap_len(l):
    h = Heap(l)
    assert len(l) == h.length()

# Using the hypothesis package to test sequentially inserting 
# integers into a heap and then sequentially deleting the 
# minimum until the heap is empty
@given(st.lists(st.integers()))
def test_heap_ins_del(l):
    h = Heap()

    for i in l:
        h.insert(i)
    
    for _ in l:
        h.delete_min()
    
    assert h.length() == 0

# Using the hypothesis package to test initializing a heap with
# a list and then sequentially deleting the minimum until the 
# heap is empty
@given(st.lists(st.integers()))
def test_heap_init_delmin(l):
    h = Heap(l)
    for _ in range(len(l)):
        h.delete_min()
    
    assert h.length() == 0

# Using the hypothesis package to test initializing a heap with
# a list and then returning a sorted version of the list
@given(st.lists(st.integers()))
def test_heap_sort(l):
    h = Heap(l)

    assert sorted(l) == h.sorted_list()


if __name__ == "__main__":
    # Test functions
    test_heap_len()
    test_heap_ins_del()
    test_heap_init_delmin()
    test_heap_sort()
