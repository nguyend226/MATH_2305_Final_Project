from functions.graph_operations import min_cost_incident_edge, inceident_edgees, initialize_tree, cost


def Prims(Graph, Starting_point):
    '''Returns the minimum sapning tree as well and the total cost of that tree. 
    Return format ( [[],()] )
    
    '''

    Tree = initialize_tree(Starting_point)
    a = inceident_edgees(Graph, Tree)
    path_to_take = min_cost_incident_edge(Graph, Tree)
 

    while (len(Tree[0]) != len(Graph[0])):                          #while the length of the tree's vertices is not the same lenght of the graph's vertices than do the operation 
        avalible_paths = inceident_edgees(Graph, Tree)          
    
        for path in avalible_paths:                                 #Checks all avalible plaths
    
             if ( path == min_cost_incident_edge(Graph, Tree)):     #Only allows for the smallest path to be taken and adds that path/edge to our working tree
                Tree[1].append(path)
                
                for edge in Tree[1]:                                #Runs through all edges in out woring tree 
    
                    for vertice in edge:                            #And vertices in those edges
    
                        if vertice not in Tree[0]:                  #And adds the vertex if it isnt in out working tree. 
                            Tree[0].append(vertice)

    return Tree

