
def inceident_edgees (Graph, Tree):
    '''Returns all posible edges that are not in the tree. Essentially give you next avalible path to the next vertex. '''

    edges_in_tree = []

    for edge in Graph[1]:

        for vertex in Tree[0]:

            if (vertex in edge) and (edge not in Tree[1]) and (edge not in edges_in_tree):
                edges_in_tree.append(edge)
    
    for edge in edges_in_tree:

        for vertex_a in Tree[0]:

            for vertex_b in Tree[0]:    

                if  ( ( '('+str(vertex_a) + ', ' + str(vertex_b)+')' ) == str(edge)   ): #Dirty fix of formating issues but got it working.
                    #If there is a edge that is in the working tree that has two of the vertices in it then remove it,
                    #by doing so we remove the posibility of have a circle in out tree
                    del edges_in_tree[ edges_in_tree.index(edge) ]
    
    return edges_in_tree


def cost (Graph,edge):
    ''' Returns the cost of an edge'''
    return Graph[1][edge]


def initialize_tree (starting_vertex):
    ''' Returns an array that is in a workable format for out other functions while ging us a starting point'''
    return (([starting_vertex],[]))


def min_cost_incident_edge(Graph,Tree):
    ''' Returns the edge with the minimum cost or shortest distance simple find the minimum in an array'''

    all_posible_new_edges = inceident_edgees(Graph,Tree)
    min_e = all_posible_new_edges[0]

    for i in all_posible_new_edges:

        if ((Graph[1][min_e] >= Graph[1][i])):
            min_e = i

    return min_e 

def total_cost_of_tree(Graph, Tree):

    total_cost_of_tree = 0
 
    for e in range(0, len( Tree[1] ) ):                             #Itterating through all the edges in the working tree.
        total_cost_of_tree = total_cost_of_tree + cost(Graph, Tree[1][e] )
        
    return total_cost_of_tree
