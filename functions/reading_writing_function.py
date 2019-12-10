import numpy as np

def get_graph(textfile):
    
    edgelist = np.loadtxt(f'data/{textfile}.txt', dtype = int ) # Grabs data from the file abd converts it in to workable data.

    Graph = ([],{})

    for edge in edgelist:      # Converts data into workable array/tuple/ditionary

        if edge[0] not in Graph[0]:
            Graph[0].append(edge[0])

        if edge[1] not in Graph[0]:
            Graph[0].append(edge[1])
            
        Graph[1][(edge[0], edge[1])] = edge[2]

    return Graph
