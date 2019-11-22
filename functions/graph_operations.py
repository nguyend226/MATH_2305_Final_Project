def inceident_edgees (G,T):
    edges = []
    for e in G[1]:
        for v in T[0]:
            if v in e and e not in T[1]:
                edges.append(e)
                #print (e)


    
    #fix the file by the weekend!!!!!!!!!!!!!!!!!!!

    ''' remove edges that make cycles goes in the fuction'''
    return edges


def cost (G,e):
    return G[1][e]


def initialize tree (v):
    return (([v],[]))


'''   '''

''' add a min_cost_incident_edge(G,T)
find the min in the list

some type of a comparitor


 '''

''' graph cost return the toatl weight of a graph   '''
