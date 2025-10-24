# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:26:56 2025

@author: loeva
"""

class Case(object):
    
    def __init__(self, num_ligne, num_colonne):
        self.num_ligne = num_ligne
        self.num_colonne = num_colonne
        
    def __str__(self):
        return("ligne   : {} \ncolonne : {}".format(self.num_ligne, self.num_colonne))



if __name__=='__main__':
    

    caseX = Case(2,3)
    
    print("Test initialisation des constructeurs :\n")
    
    print('-- ACCES AUX VALEURS')
    print("Résultat attendu : 2 3")
    print("Résultat obtenu  :", caseX.num_ligne, caseX.num_colonne)
    
    print('\n-- REDEFINITION DE PRINT')
    print(caseX)
    
    
    
    
    
    
    
    