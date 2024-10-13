#!/usr/bin/python3
"""
Pascal's triangle
"""

def pascal_triangle(n):
    """
    Return a list of lists contained in a pascal's triangle of n

    Arguments:
    n -- The size of the last list

    Returns:
    List of lists in the triangle
    """
    if n <= 0:
        return []
    
    lst = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(lst[i-1][j-1] + lst[i-1][j])
        row.append(1)
        lst.append(row)
    
    return lst
    