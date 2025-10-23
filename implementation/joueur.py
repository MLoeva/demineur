# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:23:31 2025

@author: loeva
"""

class Joueur(object):
    
    def __init__(self, nom):
        self.nom = nom
        self.score = 0
        



if __name__=='__main__':
    
    #test constructeurs
    joueur1 = Joueur('Jean')
    print("Test initialisation des constructeurs :\n")
    print("Résultat attendu : Jean")
    print("Résultat obtenu  :",joueur1.nom)