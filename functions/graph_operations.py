
def inceident_edgees (G,T):

    edges_in_tree = []

    for edge in G[1]:

        for vertice in T[0]:

            if (vertice in edge) and (edge not in T[1]) and (edge not in edges_in_tree):
                edges_in_tree.append(edge)
    
    for edge in edges_in_tree:

        for vertice_a in T[0]:

            for vertice_b in T[0]:    

                if  ( ( '('+str(vertice_a) + ', ' + str(vertice_b)+')' ) == str(edge)   ): #Dirty fix of formating issues but got it working
                    del edges_in_tree[ edges_in_tree.index(edge) ]
    
    return edges_in_tree


def cost (G,e):
    return G[1][e]


def initialize_tree (v):
    return (([v],[]))


def min_cost_incident_edge(G,T):

    all_posible_new_edges = inceident_edgees(G,T)
    min_e = all_posible_new_edges[0]

    for i in all_posible_new_edges:

        if ((G[1][min_e] >= G[1][i])):
            min_e = i

    return min_e 

def total_cost_of_tree(Graph, Tree):

    total_cost_of_tree = 0
 
    for e in range(0, len( Tree[1] ) ):                             #Itterating through all the edges in the working tree.
        total_cost_of_tree = total_cost_of_tree + cost(Graph, Tree[1][e] )
        
    return total_cost_of_tree
