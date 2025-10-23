# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:25:58 2025

@author: loeva
"""

class Grille(object):
    
    def __init__(self, nb_lignes, nb_colonnes, nb_mines):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.nb_mines = nb_mines
        



if __name__=='__main__':
    
    #test constructeurs
    grille1 = Grille(10, 12, 4)
    print("Test initialisation des constructeurs :\n")
    print("Résultat attendu : 10 12 4")
    print("Résultat obtenu  :",grille1.nb_lignes, grille1.nb_colonnes, grille1.nb_mines)