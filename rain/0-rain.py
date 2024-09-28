#!/usr/bin/python3

"""
Python Module to calculate how much rainwater is retained after it rains.
"""


def rain(waterWalls):
    """
    Calculate the square units of water will be retained after it rains.

    Arguments:
    waterWalls -- list of non-negative integers representing wall heights

    Returns:
    Integer indicating total amount of rainwater retained.
    """
    if not waterWalls:
        return 0

    left, right = 0, len(waterWalls) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if waterWalls[left] <= waterWalls[right]:
            left_max = max(left_max, waterWalls[left])
            water += left_max - waterWalls[left]
            left += 1
        else:
            right_max = max(right_max, waterWalls[right])
            water += right_max - waterWalls[right]
            right -= 1
    return water