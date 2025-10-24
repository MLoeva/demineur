# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:25:42 2025

@author: loeva
"""
#import joueur as Joueur
from grille import Grille
#import case as Case

class Partie(object):
    
    def __init__(self, niveau:int):
        self.niveau = niveau  
        self.grille_jeu = None
    
    def __str__(self):
        return( 'Niveau de la partie : {}'.format(self.niveau))
    
    def initialiserGrille(self):
        """
        Créer la grille de jeu, la taille varie avec le niveau de 
        """
        if self.niveau == 1:
            self.grille_jeu = Grille(10, 6, 4)
            self.position_mines = self.grille_jeu.calcul_position_mines() #mettre self.grille_jeu et non Grille car on fait appel à l'instance
            self.grille_numeros = self.grille_jeu.calcul_cases_numero()
            
        elif self.niveau == 2:
            self.grille_jeu = Grille(15, 10, 6)
            self.position_mines = self.grille_jeu.calcul_position_mines()
            
        elif self.niveau == 3: 
            self.grille_jeu = Grille(20, 18, 10)
            self.position_mines = self.grille_jeu.calcul_position_mines()
            
        else :
            print('ERREUR Niveaux disponibles, choisir entre 1, 2 et 3 ')
        

            
        



if __name__=='__main__':
    
    partie1 = Partie(1)
    partie1.initialiserGrille()
    print(partie1.grille_jeu)
    print('position des mines : ', partie1.grille_jeu.position_mines)
    print('grille numeros : \n', partie1.grille_jeu.grille_numeros)
    

    
    
    
    
    
    
    # print("Test initialisation des constructeurs :\n")
    
    # print('-- ACCES AUX VALEURS')
    # print("Test initialisation des constructeurs :\n")
    # print("Résultat attendu : 1")
    # print("Résultat obtenu  :",partie1.niveau)
        
    # print('\n-- REDEFINITION DE PRINT')
    # print(partie1)