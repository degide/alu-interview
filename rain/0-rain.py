#!/usr/bin/python3
"""
Python Module to calculate how much rainwater is retained after it rains.
"""


def rain(water_walls):
    """
    Calculate the square units of water will be retained after it rains.

    Arguments:
    water_walls -- list of non-negative integers representing wall heights

    Returns:
    Integer indicating total amount of rainwater retained.
    """
    if not water_walls:
        return 0

    left, right = 0, len(water_walls) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if water_walls[left] <= water_walls[right]:
            left_max = max(left_max, water_walls[left])
            water += left_max - water_walls[left]
            left += 1
        else:
            right_max = max(right_max, water_walls[right])
            water += right_max - water_walls[right]
            right -= 1
    return water
