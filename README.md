# projetAlgo
Le projet contient quatres scripts python:
1. random_graph.py
2. ALBERT_BARABASI.py 
3. twitchDE-parameters.py
4. txtToCsv.py
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
* un fichier text: "test.txt" contient les paramétres du graphe generer.
=============================================================================================================================
2.ALBERT_BARABASI.py :
  - C'est quoi?
Ce script permet de generer un graphe aléatoire a l'aide d'un paramètre d'attachement 0 < "m" < 3 et on indicant le nombre 
de noeuds final "nb_final".

  - Comment executer?
lancer la commande :
python3 ALBERT_BARABASI.py
Veuillez entrer la valeur du parametre m (m <= 3) : 2
Veuillez entrer le nombre de noeuds final :  9
  
  - Résultat de script:
* un graphe aléatoire "random_graph.png"
* un fichier text: "testALbert.txt" contient les paramétres du graphe generer.
=============================================================================================================================
3. twitchDE-parameters.py:
  - C'est quoi?
Ce script permet de  
  - Comment executer?
  
  - Résultat de script:
  
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
 
