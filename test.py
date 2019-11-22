import numpy as np
import os

from functions.reading_writing_function import get_graph
def star ():
    print ('*******')
G = get_graph('G1')

os.system("cls")
print ('*****')
print (f'V(G) = {G[0]}')
print (f'V(E) = {G[1]}')

print ('*****')


#tree


T = ([3, 1],[(1, 3)])
star()

def inceident_edgees (G,T):
    edges = []
    for e in G[1]:
        for v in T[0]:
            if v in e and e not in T[1]:
                edges.append(e)
                #print (e)
    return edges

print (inceident_edgees(G,T))