"""
9/18/17
kasim 
se.kasim.ebrahim@gmail.com
"""
import numpy as np

from Network import Network

n = Network(2,2, 2)

print "This is the random map"
print n.output_nodes, "\n\n"
# #
print "The map will reorganize itself to this value"
print np.array([n.output_nodes[0, 1]]), "\n"

data = np.array([(0, 1), (0.1, 0.9), (0.2, 0.8), (1, 0), (0.9, 0.1), (0.8, 0.2)])
# print data.shape
n.train(100, 0.1, np.array([n.output_nodes[0, 1]]))

print "this is the re organized map"
print n.output_nodes, "\n\n"
# print "\n\nth