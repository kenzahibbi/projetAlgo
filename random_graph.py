import networkx as nx
import sys
import math
import networkx
import random
import matplotlib.pyplot as plt
from networkx.generators.classic import empty_graph, path_graph, complete_graph

#fonction creation aleatoire de graph 
# Argument éntrée : n nombre de sommets
# Argument entrée : p probabilité
def aleatoire_graph(n, p):
        G=empty_graph(n) #declaration de graphe vide

        for u in range(n):
                for v in range(u+1,n):
                        if random.random() < p:
                                G.add_edge(u,v) #ajout d'un edge avec probabilité p
        return G

if __name__ == "__main__":
        n = 6 #declaration et initialisation du nombre de noeuds
        p = 0.5 #declaration et initialisation de la probabilité 

        sys.stdout = open("test.txt", "w") #ouvrir le fichier test.txt en écriture pour sauvegarder les paramétres du graphe 

        G=aleatoire_graph(n, p) #appel de la fonction pour creer un graphe aleatoire
        print(G.nodes) #écriture des nodes dans le fichier test.txt
        # [0, 1, 2, 3, 4, 5]
        print(G.edges) #écriture des edges dans le fichier test.txt
        # [(0, 1), (0, 2), (0, 4), (1, 2), (1, 5), (3, 4), (4, 5)]

        sys.stdout.close() #fermeture du flux d'ecriture

        nx.draw(G) # dessiner le graphe
        plt.savefig("random_graph.png") # sauvegarder l'image sous le nom random_graph.png
        plt.show() # Afficher le graphe
