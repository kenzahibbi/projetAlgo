import networkx as nx
import sys
import math
import networkx
import random
import matplotlib.pyplot as plt
from networkx.generators.classic import empty_graph, path_graph, complete_graph

def aleatoire_graph(n, p):
        G=empty_graph(n)

        for u in range(n):
                for v in range(u+1,n):
                        if random.random() < p:
                                G.add_edge(u,v)
        return G

if __name__ == "__main__":
        n = 6
        p = 0.5

        sys.stdout = open("test.txt", "w")

        G=aleatoire_graph(n, p)
        print(G.nodes)
        # [0, 1, 2, 3, 4, 5]
        print(G.edges)
        # [(0, 1), (0, 2), (0, 4), (1, 2), (1, 5), (3, 4), (4, 5)]

        sys.stdout.close()

        nx.draw(G)
        plt.savefig("random_graph.png")
        plt.show()
