from algorithms.prims_algorithms import Prims
import numpy as np
import os
from functions.reading_writing_function import get_graph
from functions.graph_operations import *

os.system("cls")


File = input(' get file')




Graph = get_graph("G1")

starting_point = int( input(f'{Graph[0]} /n pick a vertex')) 


minimum_spanning_tree = Prims(Graph, starting_point)


#def total_cost_of_tree (G, ):
#total_cost_of_tree = 0


for edge in range(0, len( minimum_spanning_tree) + 1 ):
    total_cost_of_tree = total_cost_of_tree + cost(Graph, minimum_spanning_tree[1][edge] )

#print(minimum_spanning_tree[1][0])

print (minimum_spanning_tree, total_cost_of_tree)