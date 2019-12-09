from functions.graph_operations import min_cost_incident_edge, inceident_edgees, initialize_tree


def Prims(Graph, Starting_point):

    Tree = initialize_tree(Starting_point)
    a = inceident_edgees(Graph, Tree)
    path_to_take = min_cost_incident_edge(Graph, Tree)
 

    while (len(Tree[0]) != len(Graph[0])):
        avalible_paths = inceident_edgees(Graph, Tree)
    
        for path in avalible_paths:
    
             if ( path == min_cost_incident_edge(Graph, Tree)):
                Tree[1].append(path)
                
                for edge in Tree[1]:
    
                    for vertice in edge:
    
                        if vertice not in Tree[0]:
                            Tree[0].append(vertice)
      
    return Tree

