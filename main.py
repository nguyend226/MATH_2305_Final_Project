from algorithms.prims_algorithms import Prims
import numpy as np
import os
from functions.reading_writing_function import get_graph
from functions.graph_operations import *

os.system("cls")


def star (somestring=''):
    
    print (f'****{somestring}****')

#File = input(' get file')




Graph = get_graph("G1")
star()
print (Graph)
star()




               



minimum_spanning_tree = Prims(Graph, 0)

total_cost_of_tree = 0


for edge in range(0, len( minimum_spanning_tree) + 1 ):
    total_cost_of_tree = total_cost_of_tree + cost(Graph, minimum_spanning_tree[1][edge] )

#print(minimum_spanning_tree[1][0])

print (minimum_spanning_tree, total_cost_of_tree)