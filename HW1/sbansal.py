import pytest
# initializing a counter to keep track of individual increasing pairs
count = 0
# initializing a variable to keep track of the longest spotted lists
maxcount = 0
# initializing a variable to store the index for the last element of
# the longest subsequence
subindex = 0

def longsubs(intlist):
    """
    Iterates through the list of integers and finds the longest 
    strictly increasing subsequence (as a list)

    Input: Integers in the form of a list
    Output: Integers part of the longest subsequence in the form of a list
    
    Note: If there are two pairs of increasing subsequences with the same
    length and the maximum length, the subsequence starting at a smaller 
    index takes precedence over the other.

    """
    count = 0
    maxcount = 0
    subindex = 0
    
    # Initial verification for if the input list of integers is blank
    if len(intlist) == 0:
        return []
    
    else:
        # Iterate through the list of integers 
        for i in range(len(intlist)-1):
            # Compare every consequent integers
            if intlist[i+1] > intlist[i]:
                # print('Checked ' + str(intlist[i+1]))
                # Increase the counter by one if the statement is true
                count += 1
                # print('Count is ' + str(count))
                # Compare the current counter to the previously stored maximum 
                # count to determine if a longer subsequence is found 
                if count > maxcount:
                    maxcount = count
                    # print('Maximum Count is ' + str(maxcount))
                    # Stores the index for the longest subsequence
                    subindex = i+1
                    # print ('Saved index is ' + str(subindex))
            # Else re-initialize the counter
            else:
                count = 0

    # Initialize a list of integers for constructing the return list
    returnlist = [0]*(maxcount+1)
    # Iterate through the longest subsequence and add integers to the return list
    for i in range(maxcount+1):
        returnlist[i] = intlist[subindex-maxcount+i]

    # Return the longest subsequence in the form of a list
    return returnlist

a = [] # Required test 1
b = [10, 9, 8, 5, 4, 1, 0] # Required test 2
c = [0, 2, 5, 6, 8, 9, 10, 15] # Required test 3
d = [9, 4, 7, 9, 10, 5, 3, 1, 3, 7, 9] # Custom test 1

def test_function():
    """
    A function to test the function using the pyTest library and documentation
    The following information conveys the tets input scenarios
    Test 1: An empty list
    Test 2: A decreasing list
    Test 3: An increasing list
    Test 4: Two pairs of longest increasing lists of the same length

    """

    assert longsubs(a) == []
    assert longsubs(b) == [10]
    assert longsubs(c) == [0, 2, 5, 6, 8, 9, 10, 15]
    assert longsubs(d) == [4, 7, 9, 10]

if __name__ == "__main__":
    # count = 0
    # maxcount = 0
    # subindex = 0
    # longsubs([6, 7, 8, 9, 10, 1, 2, 3, 4])
    a = []
    b = [10, 9, 8, 5, 4, 1, 0]
    c = [0, 2, 5, 6, 8, 9, 10, 15]
    d = [9, 4, 7, 9, 10, 5, 3, 1, 3, 7, 9]
    test_function()