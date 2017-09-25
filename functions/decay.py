"""
9/18/17
kasim 
se.kasim.ebrahim@gmail.com
"""
import numpy as np


def exponential(initial_value, iteration_index, total_iteration):
    return initial_value * np.exp(-1. * iteration_index / __decay_constant(total_iteration, initial_value))


def __decay_constant(total_iteration, initial_value):
    return total_iteration / np.log(initial_value)


def learning_rate(initial_value, iteration_index, initial_radius):
    return initial_value * np.exp(1. * iteration_index/__decay_constant(initial_radius, initial_value))

# h = 100
# for i in range(5):
#     print exponential(100, i, 5)
