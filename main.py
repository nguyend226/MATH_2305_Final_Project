from algorithms.prims_algorithms import Prims
import numpy as np
import os
from functions.reading_writing_function import get_graph
from functions.graph_operations import *

os.system("cls")


File = input(' Input name of filr that cotians the graph. :')




Graph = get_graph("G1")# Add File here

starting_point = int( input(f' {Graph[0]} \n Pick a vertex. :')) 


minimum_spanning_tree, total_cost_of_tree = Prims(Graph, starting_point)







print (f'''\n The minimun spanining tree {minimum_spanning_tree}
 and the total cost of the tree {total_cost_of_tree} ''')


