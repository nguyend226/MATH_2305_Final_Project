from functions.graph_operations import min_cost_incident_edge, inceident_edgees, initialize_tree, cost


def Prims(Graph, Starting_point):
    '''Returns the minimum sapning tree as well and the total cost of that tree. '''

    Tree = initialize_tree(Starting_point)
    a = inceident_edgees(Graph, Tree)
    path_to_take = min_cost_incident_edge(Graph, Tree)
 

    while (len(Tree[0]) != len(Graph[0])):                          #while the length of the tree's vertices is not the same lenght of the graph's vertices than do the operation 
        avalible_paths = inceident_edgees(Graph, Tree)          
    
        for path in avalible_paths:                                 #Checks all avalible plaths
    
             if ( path == min_cost_incident_edge(Graph, Tree)):
                Tree[1].append(path)
                
                for edge in Tree[1]:
    
                    for vertice in edge:
    
                        if vertice not in Tree[0]:
                            Tree[0].append(vertice)
      
    total_cost_of_tree = 0

    for e in range(0, len( Tree) + 1 ):
        total_cost_of_tree = total_cost_of_tree + cost(Graph, Tree[1][e] )


    return Tree, total_cost_of_tree

