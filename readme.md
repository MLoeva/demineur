# JEU DEMINEUR PYTHON#



## Description

Jeu du démineur ! Le but est de trouver toutes les mines cachées dans la grille de jeu sans les faire exploser.



## Bibliothèques utilisées et versions : 

numpy	1.26.4

PyQT5	5.15.7 (pour jouer avec l'interface)

random	cf version python

sys	cf version python	



Utilisation de Python 3.11.4



## Guide d'utilisation : 

Il existe 2 modes de jeu : 

* jouer dans la console : lancer le fichier implementation/partie.py
* jouer avec l'interface de jeu : lancer le fichier implementation/interface\_demineur.py



Au début de chaque partie, commencer par choisir le niveau de difficulté entre 1 et 3. NB : dans l'interface, même pour choisir le niveau 1 cliquer sur le menu déroulant et cliquer sur le niveau.



Une fois le niveau sélectionné, une grille de jeu apparait avec des 'X'. Il est temps de choisir une action : 

* creuser : pour découvrir ce qui se cacher derrière une case 'X'
* signaler : pour marquer une case où l'on suspecte qu'il y a une mine.
* désignaler : pour anuler l'action 'signaler'.



Lorsque le joueur creuse une case, derrière le 'X' se cache un numéro. Ce numéro indique le nombre de mines présentes dans les cases qui lui sont adjacentes.

Si le joueur creuse sur une case qui contenait une mine, c'est perdu. La partie est terminée, un message s'affiche pour informer le joueur.

Si le joueur réussi à signaler toutes les mines et creuser toutes les autres cases alors la partie est gagnée. De même un message l'informant de la fin de la partie s'affiche.



Un bouton de triche permet d'afficher les positions des mines et les indices permettant de les trouver.



## Nomenclature utilisée pour la grille de jeu : 

X : case non creusée

0 : case vide

2 : case numéro (aussi 1, 3, 4, 5, 6, 7, 8)

9 : mine

! : case signalée


© 11/2025 Loéva MANCEAU
