from algorithms import *

'''
make it pretty!!!!!!!!!!!!!!!!!!!!!!






'''



text = input ('please provide a graph to run the tsp on ')
text = input ('please provide a starting vertext ')

T= prims(G, v)
print (f"the optimal tre is {T}")

print('')

print (f'optimal_cost: {graph_cost(T)}')