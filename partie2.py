#!/usr/bin/env python
# coding: utf-8
 
import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#lecture du fichier csv , inserer nom fichier à analyser
f= open('test1.csv','r')
reader=csv.reader(f)

#Creation d'un dictionnaire representant le graphe, chaque sommet avec la liste des sommets formant une arrete
graph={}

for row in reader:   
    if row[0] in graph:
        # append le nouveau sommet dans la liste existante du sommet row[0]
        graph[row[0]].append(row[1])
    else:
        # creer une nouvelle liste pour le sommet row[0]
        graph[row[0]] = [row[1]] 

#creation du graphe a partir des arretes
G = nx.Graph()
for k, v in graph.items():
    G.add_edges_from(([(k, t) for t in v]))

    
#Fonctions pour recuperation des parametres
#le degre maximal: pour chaque sommet si son degre est superieur  la valeur max alors max recoit le degre du sommet i
def degre_max(G):
        max = 0
        for node in G.nodes:
            node_degree = G.degree(node)
            if node_degree > max:
                max = node_degree
        return max 

#degre moyen: calculer la somme des degres ensuite la diviser par le nombre de sommets
def degre_moyen(G):
        moyenne=0
        somme= 0
        for node in G.nodes():
            somme = somme + G.degree(node)
        
        moyenne= somme/G.number_of_nodes()
        return moyenne  

#distribution des degrés
def k_distrib(G, scale='lin', colour='#531447', alpha=.8, expct_lo=1, expct_hi=10, expct_const=1):
    
    plt.close()
    num_nodes = G.number_of_nodes()
    max_degree = 0
   
    #Calculer le degré maximum pour connaître la plage de l'axe des x 
    for n in G.nodes():
        if G.degree(n) > max_degree:
            max_degree = G.degree(n)
   
    # Valeurs des axes X et Y
    x = []
    y_tmp = []
    
    #  boucle pour tous les degrés jusqu'au maximum pour calculer la portion de nœuds pour ce degré
    for i in range(max_degree+1):
        x.append(i)
        y_tmp.append(0)
        for n in G.nodes():
            if G.degree(n) == i:
                y_tmp[i] += 1
        y = [i/num_nodes for i in y_tmp]
    # Plot le graph
    deg= plt.plot(x, y,label='Degree distribution',linewidth=0, marker='o',markersize=8, color=colour, alpha=alpha)
    
    # Vérifier le paramètre lin / log et régler l'échelle des axes
    if scale == 'log':
        plt.xscale('log')
        plt.yscale('log')
        plt.title('Degree distribution (log-log scale)')
       
        # ajouter la ligne de distribution théorique k ^ -3
        w = [a for a in range(expct_lo,expct_hi)]
        z = []
        for i in w:
            x = (i**-3) * expct_const # définir la longueur de la ligne et ajuster l'interception
            z.append(x)
        plt.plot(w,z, 'k-', color='#531447')
    else:
        plt.title('Degré de distribution ')
        
#affichage du degre de distribution   
    plt.ylabel('fréquence dapparition')
    plt.xlabel('degré')
    plt.show()

#affichage des parametres    
print("le nombre de sommet est: ",G.number_of_nodes())
print("le nombre d'arretes est: ",G.number_of_edges())
print("le degré max est: ",degre_max(G))
print("le degré moyen est: ", degre_moyen(G))
k_distrib(G)
