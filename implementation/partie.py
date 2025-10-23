# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:25:42 2025

@author: loeva
"""

class Partie(object):
    
    def __init__(self, niveau:int):
        self.niveau = niveau      
        



if __name__=='__main__':
    
    #test constructeurs
    partie1 = Partie(1)
    print("Test initialisation des constructeurs :\n")
    print("Résultat attendu : 1")
    print("Résultat obtenu  :",partie1.niveau)