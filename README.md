# projetAlgo
Le projet contient quatres scripts python:
1. random_graph.py
2. ALBERT_BARABASI.py
3. partie2.py 
4. txtToCsv.py
les librairies à installer sont: 
  *networkx
  *matplotlib
  *pandas
  *pyplot

=============================================================================================================================

1. random_graph.py :
  - C'est quoi?
Ce script permet de generer un graphe aléatoire a partir d'un nombre definie de noeud et avec une probabilité definie,
ces paramétres sont hardcoder dans le main du script, "n" (nombre de noeuds)  et "p" (probabilité).

  - Comment executer?
lancer la commande:
python3 random_graph.py

  - Résultat de script:
* un graphe aléatoire "random_graph.png"
* un fichier text: "test.txt" contient la liste des aretes du graphe generé.

=============================================================================================================================

2.ALBERT_BARABASI.py :
  - C'est quoi?
Ce script permet de generer un graphe aléatoire a l'aide d'un paramètre d'attachement 0 < "m" < 3 et on indicant le nombre 
de noeuds final "nb_final".

  - Comment executer?
lancer la commande :
python3 ALBERT_BARABASI.py
Vous devez saisir les valeurs des parametres en entrée, exemple:
Veuillez entrer la valeur du parametre m (m <= 3) : 2
Veuillez entrer le nombre de noeuds final :  9
  
  - Résultat de script:
* un graphe aléatoire affiché
* un fichier text: "testALbert.txt" contient la liste des aretes du graphe generé.

=============================================================================================================================

3. partie2.py 
 - C'est quoi?
Ce script permet de calculer les parametres suivants:Nombre de sommets, Nombre d’arêtes,Degré maximal, Degré moyen 
(somme des degrés divisée par le nombre de sommets) et La distribution des degrés.

  - Comment executer?
Avant de lancer la commande il faut mettre le nom du fichier .csv quand veut analyser (f= open('nomFichier.csv','r') )
apres exercuter la commande suivate:
python3 partie2.py

  - Résultat de script:
* une photo avec la distribution des degrés
* les differents autres parametres


=============================================================================================================================

4. txtToCsv.py :
   - C'est quoi?
Ce script sert a convertir le fichier de type text generer lors de la génération des graphe, en fichier csv
afin de les étudier dans la deuxiéme partie, le fichier text en entrée est hardcoder dans le script dans la fonction:
fin = open("test.txt", "rt"), afin de generer le fichier csv "test.csv".

  - Comment executer?
 lancer la commande: 
 python3 txtToCsv.py

- Résultat de script:
 * le fichier  "test.csv".
 
 =============================================================================================================================
 
