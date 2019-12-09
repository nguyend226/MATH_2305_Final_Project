import numpy as np

def get_graph(textfile):
    
    edgelist = np.loadtxt(f'data/{textfile}.txt', dtype = int ) # Grabs data from the file abd converts it in to workable data.

    G = ([],{})

    for x in edgelist:      # Converts data into workable array/tuple/ditionary

        if x[0] not in G[0]:
            G[0].append(x[0])

        if x[1] not in G[0]:
            G[0].append(x[1])
            

        G[1][(x[0], x[1])] = x[2]

    return G