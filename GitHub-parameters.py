#!/usr/bin/env python
# coding: utf-8

# In[162]:


import pandas as pd 
import csv 



# nom de fichier csv
filename = "GitHub.csv"
df = pd.read_csv (filename ,sep = "," )
# initialisation de la liste des titres et des lignes
fields = [] 
rows = [] 

# lecture du fichier csv
with open(filename, 'r') as csvfile: 
    # création d'un objet lecteur csv
    csvreader = csv.reader(csvfile) 
    
    # extraction des noms de champ via la première ligne 
    fields = next(csvreader) 

    # extraire chaque ligne de données une par une 
    for row in csvreader: 
        rows.append(row) 

    # obtenir le nombre total de lignes 
    print("Total nombre of rows: %d"%(csvreader.line_num)) 

# ecriture des noms de champs 
print('Field names are:' + ', '.join(field for field in fields)) 

# ecriture des 10 premières lignes 
print('\nFirst 10 rows are:\n') 
for row in rows[:10]: 
    # analyse de chaque colonne d'une ligne 
    for col in row: 
        print("%20s"%col), 
    print('\n') 



# In[163]:


#bibliotheque pour instancier des graphes
import networkx as nx
#Créer une structure de graphe vide (un «graphe nul») sans nœuds ni arêtes
G = nx.DiGraph()
#lister les edges du df
for col in df:
       for x in list(df[col]):
            G.add_edge(col,x)
            
            
        

edges=G.edges()
edges


# In[164]:


#nombre des sommets
def sommets(G):
        """ return nombre de sommets du graphe """
        return G.number_of_nodes()

sommets(G)


# In[165]:


#nombre des arretes
def edges(G):
        """ return nombre d'arrets du graphe """
        return G.number_of_edges()

edges(G)


# In[166]:


#question5
#nx.draw(G)


# In[167]:


def max_degree(G):
        """ degree maximum des sommets """
        max = 0
        for node in G.nodes:
            node_degree = G.degree(node)
            if node_degree > max:
                max = node_degree
        return max
max_degree(G)


# In[168]:


#degres moyenne
def medium_degree(G):
    moyenne=0
    nombre= 0
    for node in G.nodes():
    
        if node == "id_1" or node == "id_2":
            pass
        else:
            #ecrire (node)
            nodeint = int(node)
            nodeint += 1
            nombre = nombre + G.degree(node)
            moyenne= nombre/nodeint
    return moyenne

medium_degree(G)


# In[169]:


#IMPORTS

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import warnings


#VISUALISATION FONCTION
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
        plt.title('Degree distribution ')
        
    plt.ylabel('P(k)')
    plt.xlabel('k')
    plt.show()


# In[54]:


k_distrib(G)


# In[ ]:




