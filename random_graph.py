import networkx as nx
import matplotlib.pyplot as plt
import sys
from networkx.generators.random_graphs import erdos_renyi_graph
from random import seed
from random import randint

#n = randint(0, 10)
n = 6
p = 0.5
g = erdos_renyi_graph(n, p)

sys.stdout = open("test.txt", "w")

print(g.nodes)
# [0, 1, 2, 3, 4, 5]
print(g.edges)
# [(0, 1), (0, 2), (0, 4), (1, 2), (1, 5), (3, 4), (4, 5)]

sys.stdout.close()

nx.draw(g)
plt.savefig("random_graph.png")
plt.show()
