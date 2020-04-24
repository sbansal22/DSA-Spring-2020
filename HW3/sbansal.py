# Program for Implementing Special Queues in Python
# DSA SP20
# Author: Sparsh Bansal

import pytest

# Implementation of QuickSort 
# Reference: https://www.geeksforgeeks.org/python-program-for-quicksort/
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot, and repeats this process until the complete
# list is divided into partitions, beyond which it 
# cannot be partitioned further.

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot point
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index b
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

# Implementation of a class to define the queue object
# and the required functions
class Queue:
    # Initializing the queue object
    def __init__(self,elements=None,min=None):
        self.elements = []

    # Enqueues an element in the queue
    def enqueue(self, element):
        self.elements.insert(0, element)

    # Dequeues an element from the queue
    def dequeue(self):
        return self.elements.pop()

    # Uses Quick sort to find the min
    def findmin(self):
        min_list = self.elements
        # Checks to see if there are no elements stored in the queue
        if (len(min_list) != 0):
            quickSort(min_list,0,len(min_list)-1)
            return (min_list[0])
        else:
            return "Too few elements"


# To prove the correctness of this data structure, I have written
# some pyTest tests
def TF1():
    '''
    Test the carious functions that are applicable to queues
    
    '''
    # Define a new queue
    queue = Queue()
    assert queue.findmin() == "Too few elements"
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)
    assert queue.findmin() == 1
    queue.dequeue()
    queue.enqueue(7)
    queue.enqueue(2)
    assert queue.findmin() == 1
    queue.enqueue(1)
    assert queue.findmin() == 1

if __name__ == "__main__":
    TF1()