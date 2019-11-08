import networkx as nx
import matplotlib.pyplot as plt # For drawing

G = nx.read_edgelist('rating.txt', delimiter=",")
aux = G.edges(data=True)
B = nx.Graph()
B.add_nodes_from(list(User), bipartite=0)
B.add_nodes_from(list(Movie), bipartite=1)
B.add_edges_from(aux)

%matplotlib notebook
import [matplotlib][1].pyplot as plt
plt.figure()

edges = B.edges()
print(edges)
X, Y = bipartite.sets(B)
pos = dict()
pos.update( (n, (1, i)) for i, n in enumerate(X) ) # put nodes from X at x=1
pos.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2
nx.draw_networkx(B, pos=pos, edges=edges)
plt.show()