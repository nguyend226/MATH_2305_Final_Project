def inceident_edgees (G,T):
    edges = []
    for e in G[1]:
        for v in T[0]:
            if v in e and e not in T[1]:
                edges.append(e)
                #print (e)
    return edges
