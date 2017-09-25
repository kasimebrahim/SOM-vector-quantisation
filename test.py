"""
9/18/17
kasim 
se.kasim.ebrahim@gmail.com
"""
import numpy as np

from Network import Network
from functions import distance

n = Network(10,10, 2)

data = np.array([(0.1, 1.12), (0.034, 1.065), (0.101, 1.12), (1.01, 0.32), (1.08, 0.0301), (1.07, 0.09)])
n.train(10, 0.01, data)

point_list = []
for d in data:
    nearest_x = nearest_y = 0;
    nearest_dist = -1
    for x in range(0, n.output_x_size):
        for y in range(0, n.output_y_size):
            new_distance = distance.euclidean_squared(d,n.output_nodes[x,y])
            if nearest_dist==-1 or nearest_dist>new_distance:
                nearest_dist = new_distance
                nearest_x, nearest_y = x,y
    point_list.append((nearest_x, nearest_y))

print data
for x in range(0, n.output_x_size):
    for y in range(0, n.output_y_size):
        if point_list.count((x,y))>0:
            print "*",
        else:
            print "-",
    print ""
print point_list