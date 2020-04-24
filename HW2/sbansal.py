# Program for Implementing Doubly Linked Lists in Python
# DSA SP20
# Author: Sparsh Bansal

import pytest
import timeit
import random
import matplotlib.pyplot as plt

# Defines a single node
class Node:
    def __init__(self,val=None,next=None,prev=None):
        # Value stored in the list element
        self.val = val
        # Pointer to the next node
        self.next = next
        # Pointer to the previous node
        self.prev = prev

class DLL:
    def __init__(self,head=None,tail=None,length=None):
        ''' Constructor for an empty list '''
        self.head = None
        self.tail = None
        self.len = 0
        # Recommendation - good thing to use sentinal nodes

    def length(self):
        ''' Returns the number of nodes in the list '''
        # Method 1 - Iteration through the list - bigger O time
        # than mantaining self.len during pushes and deletes
        # 
        # i = self.head
        # count = 0
        # while i.next:
        #     i = i.next
        #     count +=1
        # return count

        # Method 2 - This class keeps track of the count as functions are called
        return self.len

    def push(self, val):
        ''' Adds a node with value equal to val to the front of the list '''

        new = Node(val)
        # Case I - when the list does not contain nodes with values
        if self.len == 0:
            self.head = new
            self.len += 1
            self.tail = new

        # Case II - when the list contains only one node with a value
        elif self.len == 1:
            new.next = self.head
            self.head.prev = new
            self.head = new
            self.tail = new.next
            self.tail.prev = self.head
            self.len += 1

        # All other cases
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
            self.len += 1

    def insert_after(self, prev_node, val):
        ''' Adds a node with value equal to val in the list after prev_node '''
        # Case for lengh = 0
        new = Node(val)
        # Case I - If the node after prev_node is the tail
        if prev_node == self.tail:
            prev_node.next = new
            new.next = None
            new.prev = prev_node
            self.tail = new
            self.len += 1

        # All other cases
        else:
            new.next = prev_node.next
            prev_node.next = new
            new.prev = prev_node
            new.next.prev = new
            self.len += 1

    def delete(self, node):
        ''' Removes node from the list '''

        #Case 0 : Case with one node
        # Case I - If the given node is the head of the list
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            self.len -= 1
        
        # Case II - if the given node is the tail of the list
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.len -= 1
        
        # All other cases
        else: 
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.len -= 1
        
    def index(self, i):
        ''' Returns the node at position i (i<n) '''
        # Include the cases for negative numbers and greater than the length
        n = self.head
        while i != 0:
            n = n.next
            i -= 1
               
        return n

    def multiply_all_pairs(self):
        ''' Multiplies all unique pairs of nodes values for nodes i, j (i != j) 
        and returns the sum '''

        # A nested for loop that mulitplies each node with every other node,
        # and then subtracts the product of each node with itself to come
        # up with the required multiplication. The last process is to divide
        # the result by the number of (nodes - 1)
        # The mathematical function used: (a + b + ....)^2

        # Method 1
        # sum = 0
        # for i in range(self.len):
        #     node = self.index(i)
        #     sum -= ((node.val)**2)
        #     for j in range(self.len):
        #         sum += ((node.val)*((self.index(j)).val))
        # return sum/2

        # Method 2
        sum = 0
        subsum = 0
        for i in range(self.len):
            node = self.index(i)
            subsum += node.val
            sum -= ((node.val)**2)
        sum += subsum**2
        return sum/2    

    def listmaker(self):
        '''
        Acknowledgement for the idea of generating this function - Casey May
        '''

        lst = []
        n = self.head
        while n != None:
            lst.append(n.val)
            n = n.next
        return lst

# Try to write tests before the program
# The first test function
def TF1():
    '''
    Tests the intialization function of the doubly linked list

    '''

    dll = DLL()
    assert dll.listmaker() == []

# The second test function
def TF2():
    '''
    Tests the length tracking of the class - uses initialization and pushes

    '''

    dll = DLL()
    assert dll.length() == 0
    dll.push(10)
    assert dll.length() == 1
    dll.push(20)
    assert dll.length() == 2
    dll.push(30)
    assert dll.length() == 3

# The third test function
def TF3():
    '''
    Tests the insert after function for the class

    '''

    dll = DLL() 
    dll.push(30)
    dll.push(20)
    assert dll.listmaker() == [20, 30]
    dll.push(10)
    assert dll.listmaker() == [10, 20, 30]
    dll.insert_after(dll.head, 40)
    assert dll.listmaker() == [10, 40, 20, 30]

# The fourth test funtion
def TF4():
    '''
    Tests the delete function of the class

    '''

    dll = DLL() 
    dll.push(30)
    dll.push(20)
    dll.push(10)
    dll.insert_after(dll.head, 40)
    dll.delete(dll.head.next)
    assert dll.listmaker() == [10, 20, 30]
    dll.delete(dll.head.next)
    assert dll.listmaker() == [10,30]

# The fifth test function
def TF5():
    '''
    Test the indexing function of the class

    '''

    dll = DLL()
    dll.push(30)
    dll.push(20)
    dll.push(10)
    dll.insert_after(dll.head, 40)
    n = dll.index(2)
    m = n.val
    assert m == 20
    dll.insert_after(dll.head, 50)
    n = dll.index(2)
    m = n.val
    assert m == 40

# The sixth test function
def TF6():
    '''
    Test the multiply all pairs function of the class
    
    '''

    dll = DLL()
    dll.push(30)
    dll.push(20)
    dll.push(10)
    assert dll.multiply_all_pairs() == 1100
    dll.delete(dll.head)
    dll.push(40)
    assert dll.multiply_all_pairs() == 2600

def Timer():
    '''
    Implements the timeit.timer function on the doubly linked list
    I have used the example code given in the assignment
    '''

    # Creating a list with 10000 entries, all equal to 1
    n = 10000
    dll = DLL()
    for i in range(n):
        dll.push(1)
        i += 1
    
    # Initializing an empty list to store the runtime averages
    timelist = []
    

    for l in range(10,10001,10):
        # Calling the index function n number of times, where n 
        # depends on the value of l and some randomization
        t = timeit.Timer('dll.index(random.randrange(l))','import random', globals=locals())
        # Computes the average runtime for 50 runs
        avgtime = t.timeit(50)
        timelist.append(avgtime)
    
    plt.plot(range(10,10001,10), timelist)
    plt.show()

def Timer2():
    '''
    Implements the timeit.timer function on the list data structure
    I have used the example code given in the assignment
    '''
   # Creating a list with 10000 entries, all equal to 0
    n = 10000
    lst = [0]*10000

    # Initializing an empty list to store the runtime averages
    timelist = []

    for l in range(10,10001,10):
        # Calling the index function n number of times, where n 
        # depends on the value of l and some randomization
        t = timeit.Timer('lst[random.randrange(l)]','import random', globals=locals())
        # Computes the average runtime for 50 runs
        avgtime = t.timeit(50)
        timelist.append(avgtime)

    plt.plot(range(10,10001,10), timelist)
    plt.show()

def Timer3():
    '''
    Implements the timeit.timer function on the doubly linked list, multiply function
    I have used the example code given in the assignment

    Note: I tried performing the runtime for up to 10000 times, but the function
    did not come to an end in reasonable amount of time.
    I tried a lot of different values, and I was able to get a quality plot
    with close to 300 times.

    The structure of the program is the same as that in Timer() and Timer2()
    '''
    avls = range(3,300)

    # Initializing an empty list to store the runtime averages
    timelist = []

    for m in range(len(avls)):
        dll = DLL()
        for n in range(avls[m]):
            dll.push(n)
        t=timeit.Timer('dll.multiply_all_pairs()', 'import random', globals=locals())
        avgtime = t.timeit(5)
        timelist.append(avgtime)
    plt.plot(avls, timelist)
    plt.show()


# In order to call test and time functions
if __name__ == "__main__":
    # PyTest calls
    # TF1()
    # TF2()
    # TF3()
    # TF4()
    # TF5()
    TF6()
    # Timer calls
    # Timer()
    # Timer2()
    # Timer3()