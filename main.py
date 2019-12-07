from algorithms import *
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




def Prims(Graph, Starting_point):

    Tree = initialize_tree(Starting_point)


    print(Tree)

    a =  inceident_edgees(Graph, Tree)
    path_to_take = min_cost_incident_edge(Graph, Tree)
 

    print (Tree)
    print (a)
    print (path_to_take)



    while (len(Tree[0]) != len(Graph[0])):
        avalible_paths = inceident_edgees(Graph, Tree)
    
        for path in avalible_paths:
             if ( path == min_cost_incident_edge(Graph, Tree)):
                Tree[1].append(path)
                
                for edge in Tree[1]:
                    #print (edge)
                    for vertice in edge:
                        if vertice not in Tree[0]:
                            Tree[0].append(vertice)
    return Tree
                #Tree.append()
    





print (Prims(Graph, 0))