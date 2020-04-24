# Author: Sparsh Bansal
# Data Structures and Algorithms SP20
# Ref: Class Ref. textbook, Introduction to Algorithms
# https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
# https://docs.python.org/2/library/random.html
# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.normal.html

import pytest
import random
import numpy

# This function finds the maximum happiness subarray
# that includes the middle food from foods
def maxhappinessmidsubarray(foods, low, mid, high):
    
    # Initializing happiness trackers
    happy = 0
    lhappy = -99999
    li = 0

    # Iterating backwards into the left subarray, starting
    # from the midpoint of the foods array (mid)

    for i in range(mid, low-1, -1):
        # Records the change in happiness on the consumption of the
        # ith element (in reverse)
        happy += foods[i]

        # Maintains the highest achieved happiness level
        if (happy > lhappy):
            lhappy = happy
            li = i

    # The next section of this function repeats the first section,
    # but this time on the right subarray of foods

    happy = 0
    rhappy = -9999
    ui = 0

    for j in range(mid+1, high+1):
        happy += foods[j]

        if (happy > rhappy):
            rhappy = happy
            ui = j
    
    # The output is the low index, the high index, and the sum
    # of the happiest subarray that includes the middle food
    # from foods
    output = []
    output.append(li)
    output.append(ui)
    output.append(lhappy+rhappy)
    return output

# This function finds the maximum happiness subarray recursively
def maxhappinesssubarray(foods, low, high):

    # This if statement handles the case when the 
    # input array contains a single food
    # When the Olin Dining Hall runs out of food?
    if high == low:
        output = []
        output.append(low)
        output.append(high)
        output.append(foods[low])
        return output
    
    else:
        mid = ((low+high)//2)
        # Below are the recursive calls
        outputl = maxhappinesssubarray(foods, low, mid)
        ls = outputl[2]
        outputr = maxhappinesssubarray(foods, mid+1, high)
        rs = outputr[2]
        outputm = maxhappinessmidsubarray(foods, low, mid, high)
        ms = outputm[2]

        # Inequalities to check which subarray has the largest
        # happiness value
        if ls >= rs and ls >= ms:
            return(outputl)
        elif rs >= ls and rs >= ms:
            return(outputr)
        else:
            return(outputm)

# Using pytest to test some edge cases
def TF1():
    
    # The case where there is only one food at the dining hall
    foods = [1]
    n = len(foods)
    max_happy = maxhappinesssubarray(foods, 0, n-1)
    assert max_happy == [0, 0, 1]

    # The case when the element after the upper index
    # of the longest happiness subarray is a 0
    foods = [1, 3, 7, 9, 0]
    n = len(foods)
    max_happy = maxhappinesssubarray(foods, 0, n-1)
    assert max_happy == [0, 3, 20]

    # The case with a negative number
    foods = [-1, 3, 7, 9, 0]
    n = len(foods)
    max_happy = maxhappinesssubarray(foods, 0, n-1)
    assert max_happy == [1, 3, 19]

    # The case where the longest array includes
    # negatives
    foods = [-1, 3, 7, 9, -3, 4, 6, 7, 10]
    n = len(foods)
    max_happy = maxhappinesssubarray(foods, 0, n-1)
    assert max_happy == [1, 8, 43]

def randomizer(ins, leng):
    """
    Creates the 100 random instances of happiness value lists
    of length n = 100, where each value is drawn uniformly between
    -10 and 10.

    """

    # Initializing an empty list to store the results
    inslist = []

    # Generates and stores the 100 different instances
    # using the library <random>
    for _ in range(leng):
        templist = []
        for _ in range(ins):
            templist.append(random.randint(-10,10))
        inslist.append(templist)

    # Test print statements for edge cases
    # print(inslist[99])
    # print(len(inslist[99]))
    return inslist

def randomizer2(ins, leng, prob, m1, sd1, m2, sd2):
    """
    A function similar to the randomizer, but using
    random.normal function

    Inputs:
    ins - number of instances
    leng - length of each instance
    prob - probability for choosing metrics 1
    m1 - mean 1
    sd1 - standard deviation 1
    m2 - mean 2
    sd2 - standard deviation 2

    """
    inslist = []

    for _ in range(leng):
        templist = []
        for _ in range(ins):
            p = random.uniform(0, 1)

            # According to the given probability, I pick b/w 
            # choosing metrics 1 or 2
            if p <= prob:
                templist.append((numpy.random.normal(m1, sd1, 1))[0])
            else:
                templist.append((numpy.random.normal(m2, sd2, 1))[0])
        
        inslist.append(templist)
    
    # Test print statements for edge cases
    # print(inslist[99])
    # print(len(inslist[99]))

    return inslist

def avglenfind():
    """
    Function that computes the average maximum happiness
    across the 100 instances generated by the randomizer()

    """

    # Calls the function randomizer defined above to get
    # the set of 100 instances
    # inslist = randomizer(100,100)
    inslist = randomizer2(100, 100, 0.7, 6, 1, -7, 0.5)
    recsum = []
    reclen = []
    ttlsum = 0
    ttllen = 0
    k = 0

    # For each of the 100 instances stored in inslist, 
    # run the maximum happiness finder and record the 
    # results
    for k in range(len(inslist)):
        templist = maxhappinesssubarray(inslist[k], 0, len(inslist)-1)
        recsum.append(templist[2])
        ttlsum += templist[2]
        reclen.append(templist[1]-templist[0])
        ttllen += (templist[1]-templist[0])

    
    # Calculates the mean sum
    avgsum = ttlsum/len(inslist)
    avglen = ttllen/len(inslist)
    
    # Test print statement
    print(avgsum)
    print(avglen)

    return avglen, avgsum

if __name__ == "__main__":
    # TF1()
    # randomizer(100,100)
    avglenfind()
    # randomizer2(100, 100, 0.7, 6, 1, -7, 0.5)