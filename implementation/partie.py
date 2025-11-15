# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:25:42 2025

@author: loeva
"""

from grille import Grille

class Partie(object):
    
    def __init__(self, niveau:int):
        """
        Initialise une nouvelle partie de démineur.

        Paramètres
        ----------
        niveau : int
            Niveau de difficulté choisi par le joueur.
            (Exemples possibles : 1 = facile, 2 = moyen, 3 = difficile)

        Description
        -----------
        Cette classe représente une partie de démineur en cours.
        """
        
        self.niveau = niveau  
        self.grille_jeu = None
    
    def __str__(self):
        return( 'Niveau de la partie : {}'.format(self.niveau))
    
    def initialiserGrille(self):
        """

        Initialise la grille de jeu en fonction du niveau choisi.
      
        Description
        -----------
        Cette méthode crée une instance de `Grille` adaptée au niveau de 
        difficulté sélectionné par le joueur.

      
        Après la création de la grille, la méthode :
            - calcule les positions des mines,
            - calcule les valeurs numériques associées à chaque case
              (nombre de mines voisines),
            - stocke ces informations dans les attributs de la classe `Grille`.
        """
        
        if self.niveau == 1:
            #self.grille_jeu = Grille(10, 10, 6)
            self.grille_jeu = Grille(5, 5, 5)
            self.grille_jeu.calcul_position_mines() #mettre self.grille_jeu et non Grille car on fait appel à l'instance
            self.grille_jeu.calcul_cases_numero()
            
        elif self.niveau == 2:
            self.grille_jeu = Grille(15, 15, 30)
            self.grille_jeu.calcul_position_mines()
            self.grille_jeu.calcul_cases_numero()
            
        elif self.niveau == 3: 
            self.grille_jeu = Grille(20, 20, 40)
            self.grille_jeu.calcul_position_mines()
            self.grille_jeu.calcul_cases_numero()
            
        else :
            print('ERREUR Niveau indisponibles, merci de choisir entre 1, 2 ou 3 ')

            
    def creuser_case(self, ligne, colonne):
        """
        Tente de creuser une case dans la grille de jeu.
    
        Paramètres
        ----------
        ligne : int
            Ligne de la case que le joueur souhaite creuser.
        colonne : int
            Colonne de la case que le joueur souhaite creuser.
    
        Description
        -----------
        Cette méthode appelle la fonction `creuser` de la grille (`Grille.creuser`) 
        pour révéler le contenu de la case sélectionnée.
    
        - Si la case contient une mine (`creuser` renvoie True) :
            - La partie est perdue
        - Sinon :
            - La partie continue.
    
        Retour
        ------
        bool
            True  -> le joueur a perdu en creusant une mine.
            False -> le joueur peut continuer à jouer.
        """
        resultat = self.grille_jeu.creuser(ligne, colonne)
        
        if resultat is True: #j'ai perdu
            self.gagner_partie(False)
            return True
        
        return False

    def signaler_case(self, ligne, colonne):
        """
        Signale (pose un drapeau) sur une case de la grille de jeu.

        Paramètres
        ----------
        ligne : int
            Ligne de la case à signaler.
        colonne : int
            Colonne de la case à signaler.
    
        Description
        -----------
        Cette méthode appelle la fonction `signaler` de la grille (`Grille.signaler`)
        pour marquer la case spécifiée avec un drapeau ('!').

        """
        
        self.grille_jeu.signaler(ligne, colonne)


    def designaler_case(self, ligne, colonne):
        """
        Déignale (retire un drapeau) sur une case de la grille de jeu.

        Paramètres
        ----------
        ligne : int
            Ligne de la case à désignaler.
        colonne : int
            Colonne de la case à désignaler.
    
        Description
        -----------
        Cette méthode appelle la fonction `designaler` de la grille (`Grille.designaler`)
        pour dé-marquer la case spécifiée avec un drapeau ('!').

        """
        self.grille_jeu.designaler(ligne, colonne)
        
        
        
# =============================================================================    
#     Fonctions pour jouer dans la console    
# =============================================================================
    def jouer(self):
        """
        Boucle principale pour jouer une partie de démineur DANS LA CONSOLE.
    
        Description
        -----------
        Cette méthode gère l'interaction avec le joueur dans la console :
        - Elle demande au joueur quelle action effectuer :
            - 'C' : creuser une case,
            - 'S' : signaler une mine,
            - 'D' : retirer un drapeau (designaler).
        - Elle demande ensuite sur quelle case appliquer l'action, au format "ligne colonne".
        - Les actions sont répétées dans une boucle jusqu'à la fin de la partie 
          (défaite ou victoire).
        """
      
        resultat = False
        while resultat == False:
            try :
                action = input('Quelle action faire ? (creuser(C), signaler(S), designaler(D))')
                case = input('Sur quelle case ? (Répondre au format : ligne colonne').split()
            
                
                if action == 'C': 
                    resultat = self.grille_jeu.creuser(int(case[0]),int(case[1]))
                    print(self.grille_jeu)
                    self.gagner_partie(resultat)
                    #print('RESULTAT', resultat)
                    
                elif action == 'S' :
                    self.grille_jeu.signaler(int(case[0]),int(case[1]))
                    print(self.grille_jeu)
                    
                elif action== 'D':
                    self.grille_jeu.designaler(int(case[0]),int(case[1]))
                    print(self.grille_jeu)
                
                else :
                    print('\nERREUR Veuillez choisir une action parmi : creuser, signaler, designaler\n')
        
        
                if sum(sum(self.grille_jeu.grille_visible == 'X')) == 0:
                    resultat = True
                    self.gagner_partie(resultat)
                    break
                
            except IndexError : 
                print('\nERREUR Veuiller choisir une case DANS la grille\n')
        
                    
            
    def gagner_partie(self, issue:bool): #fonction inutile
        """
        Affiche le message correspondant à l’issue de la partie.
      
        Paramètres
        ----------
        issue : bool
            True  -> le joueur a gagné la partie.
            False -> le joueur a perdu en creusant une mine.
        """
        
        if issue == True :
            print("BRAVO ! Tu as gagné !")
            #prob : on peut gagner si on signale toute la grille
        
        if issue == False :
            print("Oh oh.. tu viens de tout faire exploser")
            print("\nFIN DU JEU\n")
            print("\nNB : faire ctrl+c pour arrêter la partie\n")
            

                

if __name__=='__main__':
    
    
    niveau = int(input('Choisi le niveau de difficulté : (1,2 ou 3)'))
    print('Voici la grille de jeu')
    partie_en_cours = Partie(niveau)
    partie_en_cours.initialiserGrille()
    print(partie_en_cours.grille_jeu)
    partie_en_cours.jouer()
    
    
    #TESTS
    
    # print('INITIALISER LA GRILLE DE JEU' )
    # print('Cas où on renseigne un niveau non disponible (>3):')
    # partie0 = Partie(6)
    # partie0.initialiserGrille()
    
    # print('\n\nCas où on renseigne un niveau disponible (<=3):')
    # print("(il n'y a pas de message d'erreur)")
    # partie1 = Partie(1)
    # partie1.initialiserGrille()
    
    
    # print('\n\nDIFFERENTS NIVEAUX')
    # print('NIVEAU 1')
    # print('Grille visible :')
    # print(partie1.grille_jeu)
    # print('\nGrille cachée : ')
    # print(partie1.grille_jeu.grille_numeros)
    
    # print('\n\nNIVEAU 2')
    # partie2 = Partie(2)
    # partie2.initialiserGrille()
    # print('Grille visible :')
    # print(partie2.grille_jeu)
    # print('\nGrille cachée : ')
    # print(partie2.grille_jeu.grille_numeros)
    
    # print('\n\nNIVEAU 3')
    # partie3 = Partie(3)
    # partie3.initialiserGrille()
    # print('Grille visible :')
    # print(partie3.grille_jeu)
    # print('\nGrille cachée : ')
    # print(partie3.grille_jeu.grille_numeros)
    
    # print('\n\nCREUSER')
    # print("Résultat attendu : \nLa grille est composée uniquement de 'X' à l'exception de la case (3,3) qui affiche un numéro. De plus, un message d'encouragement s'affiche.\n")
    # resultat = partie1.grille_jeu.creuser(3,3)
    # partie1.finPartie()
    # print(partie1.grille_jeu)
    
    # print('\n\nSIGNALER')
    # print("Résultat attendu : \nLa grille est composée uniquement de 'X' à l'exception de la case creusée précédemment et de la case (3,4) qui affiche un '!'.\n")
    # partie1.grille_jeu.signaler(3,4)
    # print(partie1.grille_jeu)
    
    # print('\n\nDESIGNALER')
    # print("La case (3,4) est à nouveau affichée comme 'X'\n")
    # partie1.grille_jeu.designaler(3,4)
    # print(partie1.grille_jeu)
    #
    #print('position des mines : ', partie1.grille_jeu.position_mines)
    #print('grille numeros : \n', partie1.grille_jeu.grille_numeros)