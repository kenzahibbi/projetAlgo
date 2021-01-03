#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd 
import csv 

df = pd.read_csv (file ,sep = "," )

# nom de fichier csv
filename = "twitchDE.csv"
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
		print("%10s"%col), 
	print('\n') 








# In[44]:


#biblio pour instancier des graphes
import networkx as nx
#Créez une structure de graphe vide (un «graphe nul») sans nœuds ni arêtes
G = nx.DiGraph()
#lister les edges du df
for col in df:
       for x in list(df[col]):
            G.add_edge(col,x)
            
            
        

edges=G.edges()
edges


# In[45]:


#nombre des sommets
def sommets(G):
        """ return nombre de sommets du graphe """
        return G.number_of_nodes()

sommets(G)


# In[46]:


#nombre des arretes
def edges(G):
        """ return nombre d'arrets du graphe """
        return G.number_of_edges()

edges(G)


# In[37]:


#nx.draw(G)


# In[47]:


def max_degree(G):
        """ degree maximum des sommets """
        max = 0
        for sommet in G.nodes:
            sommet_degree = G.degree(sommet)
            if sommet_degree > max:
                max = sommet_degree
        return max
max_degree(G)


# In[48]:


#degres moyenne
nombre= 0
for somme in G.nodes():
    
    if somme == "from" or somme == "to":
        pass
    else:
        #print (somme)
        sommeint = int(somme)
        sommeint += 1
        nombre = nombre + G.degree(somme)
        moyenne= nombre/sommeint

moyenne


# In[ ]:





# In[ ]:




