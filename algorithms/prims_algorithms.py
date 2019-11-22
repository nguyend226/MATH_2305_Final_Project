"""" prims goes here  """


def prims (textfile)
    G = get_graph(textfile )
    T = initialize_tree(G ,v)
    
    while T[0] != G[0]
        e = min_cost_edges(G,T)
    #add e and it verticeis to T......
        return T