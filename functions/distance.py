"""
9/18/17
kasim 
se.kasim.ebrahim@gmail.com
"""
import numpy as np


def euclidean_squared(v, w):
    sum = 0
    for _v, _w in zip(v, w):
        sum += np.square(_v - _w)
    return sum


# print euclidean_squared(np.array([1, 2, 3]), np.array([0, 0, 0]))
