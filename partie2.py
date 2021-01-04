import csv
import networkx as nx
import matplotlib.pyplot as plt


f= open('testAlbert4.csv','r')
reader=csv.reader(f)
# initialisation de la liste des titres et des lignes

graph={}

for row in reader:  
    for row in reader:  
        if row[0] in graph:
            # append the new number to the existing array at this slot
            graph[row[0]].append(row[1])
        else:
            # create a new array in this slot
            graph[row[0]] = [row[1]] 
        
G = nx.Graph()
for k, v in graph.items():
    G.add_edges_from(([(k, t) for t in v]))

def param(G):
        """ return nombre d'arrets du graphe """
        i=G.number_of_edges()
        j=G.number_of_nodes()
        """degre max"""
        max = 0
        for node in G.nodes:
            node_degree = G.degree(node)
            if node_degree > max:
                max = node_degree
                
        moyenne=0
        nombre= 0
        for node in G.nodes():
            #ecrire (node)
            nodeint = int(node)
            nodeint += 1
            nombre = nombre + G.degree(node)
            moyenne= nombre/nodeint
       
        return j,i,max,moyenne  


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
    plt.savefig("random_graph.png")
    plt.show()

print(param(G))
k_distrib(G)
