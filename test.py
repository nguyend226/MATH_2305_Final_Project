import numpy as np
import os
from functions.reading_writing_function import get_graph
from functions.graph_operations import inceident_edgees, cost


def star ():
    print ('*******')


G = get_graph('G1')

os.system("cls")
star()
print (f'V(G) = {G[0]}')
print (f'V(E) = {G[1]}')
star()

#tree


T = ([3, 1, 4], [(1, 3), (1, 4)])

'''
star()
for e in G[1]:
    print (e)
star()

'''
#print (inceident_edgees(G,T))

print(f'T={T}')

star()
for e in inceident_edgees(G,T):
    print (f"Edge {e} with the cost {cost(G, e)}")
star()
