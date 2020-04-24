# Program for Homework 09
# DSA SP20
# Author: Sparsh Bansal
# Reference: Teaching Team, Cassandra Overney

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
    # if b == 0:
    #     return a==0
    # Pre-processing to ensure that multiple wildcard characters
    # are replaced by a single wildcard character since they are
    # equivalent

    # # Edge Case - when the pattern is a single star
    # if b == 1 and s2 == '*':
    #     return True

    # Approach A - Using the bottom-up technique. Here I calculate and store
    # all the subproblems
    # results = [[False for x in range(b+1)] for y in range(a+1)]
    results = np.zeros((a+1, b+1), dtype=bool)

    results[0][0] = True

    # Add the base cases
    # the rest of the elements in the first row are False except if all
    # the previous chars are '*'
    for j in range(results.shape[1]):
        if j == 0:
            continue
        elif s2[j-1] == "*" and results[0][j-1]:
            results[0][j] = True

    # if b > 0 and s2[0] == '*':
    #     for l in range(len(results)):
    #         results[l][1] = True

    for i in range(1,results.shape[0]):
        for j in range(1,results.shape[1]):
            if s1[i-1] == s2[j-1]:
                results[i][j] = results[i-1][j-1]
            elif s2[j-1] == '*':
                results[i][j] = results[i-1][j] or results[i][j-1]

    return results[results.shape[0]-1][results.shape[1]-1]

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
    Test 8 - Input is a null string and pattern is a single wildcard character
    """

    assert wildcardmatcher('Lemondrop', '*******Le*******dr******p*******') == True
    assert wildcardmatcher('Lemondrop', 'Lem**dr*p*') == True
    assert wildcardmatcher('Sparsh', '*') == True
    assert wildcardmatcher('Sparsh', '') == False
    assert wildcardmatcher(' ', '*********') == True
    assert wildcardmatcher('Lemondrop', 'L*mk*dr*p') == False
    assert wildcardmatcher('','') == True
    assert wildcardmatcher(' ', '*') == True
    assert wildcardmatcher('', '*') == True

if __name__ == "__main__":
    test_function()