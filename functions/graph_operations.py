def inceident_edgees (G,T):

    edges_in_tree = []


    for edge in G[1]:
#        print(edge)
        for vertice in T[0]:
#            print(vertice)
            if (vertice in edge) and (edge not in T[1]) and (edge not in edges_in_tree) and (vertice not in ((T[]) or (False))  ) :
                edges_in_tree.append(edge)

 




    #fix the file by the weekend!!!!!!!!!!!!!!!!!!!

    ''' remove edges that make cycles goes in the fuction'''
    return edges_in_tree


def cost (G,e):
    return G[1][e]


def initialize_tree (v):
    return (([v],[]))



def min_cost_incident_edge(G,T):

    all_posible_new_edges = inceident_edgees(G,T)
    min_e=all_posible_new_edges[0]

    for i in all_posible_new_edges:
        print (f"{i} , {min_e} ,  {G[1][i]}")
        if ((G[1][min_e] >= G[1][i])):   # and  (i not in T[1])  ):
            min_e = i

    return min_e , G[1][min_e]




#            pass

#        if (all_posible_new_edges[1][i] <= all_posible_new_edges[1][i+1]):
#            ar.append((all_posible_new_edges[1][i]))
    

#    return ar    
    #arr = [[], []]

    #for new_edge in all_posible_new_edges:
    #    arr[0].append(new_edge)
    #    arr[1].append(G[1][new_edge])
    

    #return all_posible_new_edges


    '''
    ar = []
    qw = []
    for i in G[1]:
        ar.append(i)
    for q in G[1]:
        qw.append(G[1][q])
    return qw
    '''






    '''
        edges_in_tree = []
    for e in G[1]:
        for v in T[0]:
            if v in e and e not in T[1]:
                edges_in_tree.append(e)

    return edges_in_tree

    '''


    '''
    edge_in_tree = []

    for edge in G[1]:
        for vertice in T[0]:
            pass
#            if vertice in edge >= G[][]:
#    for edge in T:
#        pass

    '''

#find the min in the list

#some type of a comparitor




''' graph cost return the toatl weight of a graph   '''
