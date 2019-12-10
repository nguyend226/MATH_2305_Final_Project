from functions.graph_operations import min_cost_incident_edge, incident_edges, initialize_tree, cost


def Prims(Graph, Starting_point):
    '''Returns the minimum sapning tree as well and the total cost of that tree. 
    Return format ( [[],()] )
    
    '''

    Tree = initialize_tree(Starting_point)
    avalible_paths = incident_edges(Graph, Tree)          
    path_to_take = min_cost_incident_edge(Graph, Tree)


    while (len(Tree[0]) != len(Graph[0])):                          #while the length of the tree's vertices is not the same lenght of the graph's vertices than do the operation 
    
        for path in avalible_paths:                                 #Checks all avalible plaths

            for vertex_a in Tree[0]:

                for vertex_b in Tree[0]:                        

                    if ( path == min_cost_incident_edge(Graph, Tree)) and ( str(path) != '(' + str (vertex_a) + ', ' + str(vertex_b) + ')' ):     #Only allows for the smallest path to be taken and adds that path/edge to our working tree  
                        Tree[1].append(path)
        
            for edge in Tree[1]:                                #Runs through all edges in out woring tree 

                for vertice in edge:                            #And vertices in those edges

                    if vertice not in Tree[0]:                  #And adds the vertex if it isnt in out working tree. 
                        Tree[0].append(vertice)
                        avalible_paths = incident_edges(Graph, Tree)          
                        path_to_take = min_cost_incident_edge(Graph, Tree)  
            

    return Tree
