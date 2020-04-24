# Program for Homework 09
# DSA SP20
# Author: Sparsh Bansal

import pytest
import numpy as np


def wildcardmatcher(s1,s2):
    """
    Finds whether there exists a substitution into the wildcard 
    characters such that the end result yields s1.
    
    Input:
    s1 - a fixed string of characters a-z
    s2 - a string that may contain one or more wildcard 
    characters which represent any possible substring

    """

    # Assigning the lengths of the two strings
    a = len(s1)
    b = len(s2)

    # If the length of the pattern string is 0,
    # the condition is true if and only if 
    # length of the input string is also 0
    if b == 0:
        return a==0
    # Pre-processing to ensure that multiple wildcard characters 
    # are replaced by a single wildcard character since they are 
    # equivalent

    # Getting rid of the extra wildcard characters
    lists2 = list(s2.strip())
    news2 = ''
    for k in range(1,len(lists2)):
        if lists2[k] == '*':
            if lists2[k-1] != '*':
                news2 += lists2[k]  
        else:
            news2 += lists2[k]
    
    # This is the new pattern string, news2
    news2 = lists2[0] + news2

    # Upadting the length of this string
    b = len(news2)

    # Approach A - Using the bottom-up technique. Here I calculate and store
    # all the subproblems
    # results = [[False for x in range(len(s1)+1)] for y in range(len(news2)+1)]

    # Add the base case
    
    # if len(news2)-1 > 0 and news2[0] == '*':  
    #     results[0][1] = True
    
    # results[0][0] = True

    # for i in range(1,len(results)):
    #     for j in range(1,len(results[0])):
    #         if s1[i-1] == news2[j-1]:
    #             results[i][j] = results[i-1][j-1]
    #         elif news2[j-1] == '*':
    #             results[i][j] = results[i-1][j] or results[i][j-1]

    # -----------------------------------------------------------------------------------

    # Approach B - Using the bottom up technique. Checking for the final
    # indices of the given strings

    # Initializing variables
    s2 = news2
    ai = 0
    bi = 0
    s = 0

    while ai <= a-1:

        # The case when the characters are identical in the two strings
        if bi < b and s1[ai] == s2[bi]:

            # We just move forward in both string by one index position
            ai += 1
            bi += 1
        
        # The case when string 2 hits a star
        elif bi < b and s2[bi] == '*':
            bi += 1
            s += 1
            # Checks to see if the character next to the star in string 2
            # matches the character in string 1 OR if we have reached the end
            # of string 2
            if bi == b or s2[bi] == s1[ai]:
                return True
        
        # The case when string 2 has not hit a star
        elif bi < b and s2[bi] != '*':
            # Checks to see if the character in string 1 is equal 
            # to that in string 2 or not, and if we have the possibility
            # of using the wildcard character to work for the case
            if s1[ai] != s2[bi] and s == 0:
                return False
            else:
                ai += 1
                bi += 1
        # If none of the above cases are true, we exit out of the while loop here
        else:
            return False
    # Return False as a default result
    return False

    # -----------------------------------------------------------------------------------


def test_function():
    """
    Test function for wildcardmatcher
    Test 1 - More than necessary number of wildcard characters
    Test 2 - Adequate number of wildcard characters
    Test 3 - The whole of the pattern is a wildcard
    Test 4 - The pattern string is a null string
    Test 5 - The input string is single character empty
    Test 6 - The pattern string has one extra character than required
    Test 7 - Both strings are null strings
    """

    assert wildcardmatcher('Lemondrop', '*******Le*******dr******p*******') == True
    assert wildcardmatcher('Lemondrop', 'Lem**dr*p*') == True
    assert wildcardmatcher('Sparsh', '*') == True
    assert wildcardmatcher('Sparsh', '') == False
    assert wildcardmatcher(' ', '*********') == True
    assert wildcardmatcher('Lemondrop', 'L*mk*dr*p') == False  
    assert wildcardmatcher('','') == True  
    assert wildcardmatcher(' ', '*') == True

if __name__ == "__main__":
    test_function()