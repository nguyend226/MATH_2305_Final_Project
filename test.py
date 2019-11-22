import numpy as np
import os
from functions.reading_writing_function import get_graph
from functions.graph_operations import inceident_edgees


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

#print (inceident_edgees(G,T))