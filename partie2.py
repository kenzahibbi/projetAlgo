{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(600, 1196, 61, 4.27906976744186)\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import csv\n",
    "import networkx as nx\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "f= open('testAlbert4.csv','r')\n",
    "reader=csv.reader(f)\n",
    "# initialisation de la liste des titres et des lignes\n",
    "\n",
    "graph={}\n",
    "\n",
    "for row in reader:  \n",
    "    for row in reader:  \n",
    "        if row[0] in graph:\n",
    "            # append the new number to the existing array at this slot\n",
    "            graph[row[0]].append(row[1])\n",
    "        else:\n",
    "            # create a new array in this slot\n",
    "            graph[row[0]] = [row[1]] \n",
    "        \n",
    "G = nx.Graph()\n",
    "for k, v in graph.items():\n",
    "    G.add_edges_from(([(k, t) for t in v]))\n",
    "\n",
    "def param(G):\n",
    "        \"\"\" return nombre d'arrets du graphe \"\"\"\n",
    "        i=G.number_of_edges()\n",
    "        j=G.number_of_nodes()\n",
    "        \"\"\"degre max\"\"\"\n",
    "        max = 0\n",
    "        for node in G.nodes:\n",
    "            node_degree = G.degree(node)\n",
    "            if node_degree > max:\n",
    "                max = node_degree\n",
    "                \n",
    "        moyenne=0\n",
    "        nombre= 0\n",
    "        for node in G.nodes():\n",
    "            #ecrire (node)\n",
    "            nodeint = int(node)\n",
    "            nodeint += 1\n",
    "            nombre = nombre + G.degree(node)\n",
    "            moyenne= nombre/nodeint\n",
    "       \n",
    "        return j,i,max,moyenne  \n",
    "\n",
    "\n",
    "def k_distrib(G, scale='lin', colour='#531447', alpha=.8, expct_lo=1, expct_hi=10, expct_const=1):\n",
    "    plt.close()\n",
    "    num_nodes = G.number_of_nodes()\n",
    "    max_degree = 0\n",
    "    #Calculer le degré maximum pour connaître la plage de l'axe des x \n",
    "    for n in G.nodes():\n",
    "        if G.degree(n) > max_degree:\n",
    "            max_degree = G.degree(n)\n",
    "    # Valeurs des axes X et Y\n",
    "    x = []\n",
    "    y_tmp = []\n",
    "    #  boucle pour tous les degrés jusqu'au maximum pour calculer la portion de nœuds pour ce degré\n",
    "    for i in range(max_degree+1):\n",
    "        x.append(i)\n",
    "        y_tmp.append(0)\n",
    "        for n in G.nodes():\n",
    "            if G.degree(n) == i:\n",
    "                y_tmp[i] += 1\n",
    "        y = [i/num_nodes for i in y_tmp]\n",
    "    # Plot le graph\n",
    "    deg= plt.plot(x, y,label='Degree distribution',linewidth=0, marker='o',markersize=8, color=colour, alpha=alpha)\n",
    "    # Vérifier le paramètre lin / log et régler l'échelle des axes\n",
    "    if scale == 'log':\n",
    "        plt.xscale('log')\n",
    "        plt.yscale('log')\n",
    "        plt.title('Degree distribution (log-log scale)')\n",
    "        # ajouter la ligne de distribution théorique k ^ -3\n",
    "        w = [a for a in range(expct_lo,expct_hi)]\n",
    "        z = []\n",
    "        for i in w:\n",
    "            x = (i**-3) * expct_const # définir la longueur de la ligne et ajuster l'interception\n",
    "            z.append(x)\n",
    "        plt.plot(w,z, 'k-', color='#531447')\n",
    "    else:\n",
    "        plt.title('Degree distribution ')\n",
    "        \n",
    "    \n",
    "    plt.ylabel('P(k)')\n",
    "    plt.xlabel('k')\n",
    "    plt.savefig(\"random_graph.png\")\n",
    "    plt.show()\n",
    "\n",
    "print(param(G))\n",
    "k_distrib(G)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "61"
      ]
     },
     "execution_count": 226,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.27906976744186"
      ]
     },
     "execution_count": 227,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "medium_degree(G)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
