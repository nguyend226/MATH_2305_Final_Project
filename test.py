from algorithms.prims_algorithms import Prims
import numpy as np
import os
from functions.reading_writing_function import get_graph
from functions.graph_operations import *

os.system("cls") # used to clear the console on windows machines


File = input(' Input name of file that cotians the graph. :')




Graph = get_graph('G'+File) 

starting_point = int( input(f' {Graph[0]} \n Pick a vertex. :')) 

minimum_spanning_tree = Prims(Graph, starting_point)
cost_of_tree = total_cost_of_tree(Graph, minimum_spanning_tree)

vertices, edges = minimum_spanning_tree

T =  ([0, 1, 4], [(0, 1), (1, 4)])

print (f'''\n The minimun spanining tree 
 Vetices: {vertices}, {len(vertices)}
 Edges : {edges}, {len(edges)}
 and the total cost of the tree {total_cost_of_tree(Graph, minimum_spanning_tree)} 
 ********* prims output **********
 {minimum_spanning_tree}
******** incident_edges **********
T =   {T}
avalible paths to get last vertex. 
{incident_edges(Graph, T)}
 ''')
