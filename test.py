import numpy as np
import os
from functions.reading_writing_function import get_graph
from functions.graph_operations import *
os.system("cls")


def star (somestring=''):
    
    print (f'****{somestring}****')


G = get_graph('G1')

os.system("cls")

star('raw graph')
print (G)

star('graph simplyfied')

print (f'G(V) = {G[0]}')

print (f'G(E) = {G[1]}')

print (f'G(cost) = {G[1].values() }')

star()



#start point on tree ? 
#T = ([3, 1, 4 ], [(1, 3), (1, 4)])
#T = ([0,1,3,2], [(0,1), (1,3), (2,3)])

T = ([5], [])

star("all edges")
for e in G[1]:
    print (e)
star()

print (inceident_edgees(G,T))

print(f'Tree={T}')

star("All incident edges")
for e in inceident_edgees(G,T):
    print (f"Edge {e}")# with the cost {cost(G, e)}")
star()


star(f'{T[0]}')

star("cost of 1,3")
print (f"{cost(G, (1,3))}")
star()

star("min_cost_incedent_edge")
print (f"{ min_cost_incident_edge (G, T)}")
star()



star('new section incenden testing')

print (f'{inceident_edgees(G,T)}')
#print(f"{g}")

star()








