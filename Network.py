"""
9/18/17
kasim 
se.kasim.ebrahim@gmail.com
"""

import numpy as np
import functions
from functions import decay
from functions import distance


class Network:
    def __init__(self, output_x_size, output_y_size, input_size):
        self.output_x_size = output_x_size
        self.output_y_size = output_y_size
        self.input_size = input_size

        self.n_radius = self.initial_radius = max(output_x_size, output_y_size) / 2
        self.output_nodes = np.random.randn(output_x_size, output_y_size, input_size)

    def train(self, epoch, eta, data):
        initial_eta = eta
        for iteration in range(epoch):

            eta = decay.learning_rate(initial_eta, iteration, epoch)
            self.n_radius = int(decay.exponential(self.initial_radius, iteration, epoch))

            _input = data[np.random.randint(0, data.shape[0] - 1)]
            best_match_x, best_match_y = self.find_best_match(_input)

            min_x = best_match_x - self.n_radius
            max_x = best_match_x + self.n_radius+1
            min_x = 0 if min_x < 0 else min_x
            max_x = self.output_x_size if max_x > self.output_x_size else max_x
            for _x in range(min_x, max_x):
                min_y = best_match_y - self.n_radius
                max_y = best_match_y + self.n_radius+1
                min_y = 0 if min_y < 0 else min_y
                max_y = self.output_y_size if max_y > self.output_y_size else max_y
                for _y in range(min_y, max_y):
                    distance_influence = np.exp(
                        -1. * distance.euclidean_squared(np.array([best_match_x, best_match_y]), np.array([_x, _y])) / (
                            2 * self.n_radius ** 2))
                    change = distance_influence * initial_eta * (_input - self.output_nodes[_x, _y])
                    self.output_nodes[_x, _y] = self.output_nodes[_x, _y] + change

    def find_best_match(self, _input):
        best_distance = -1
        best_x = best_y = -1
        for x in range(self.output_x_size):
            for y in range(self.output_y_size):
                new_distance = distance.euclidean_squared(self.output_nodes[x, y], _input)
                if best_distance == -1 or best_distance > new_distance:
                    best_distance = new_distance
                    best_x, best_y = x, y
        return best_x, best_y
