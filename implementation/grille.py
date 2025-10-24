# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:25:58 2025

@author: loeva
"""
import numpy as np
import random as rd

class Grille(object):
    
    def __init__(self, nb_lignes, nb_colonnes, nb_mines):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.grille_visible = np.array(['X' for _ in range(self.nb_lignes*self.nb_colonnes)]).reshape((self.nb_lignes,self.nb_colonnes))
        self.nb_mines = nb_mines
        self.position_mines = []
        self.grille_numeros = np.zeros((self.nb_lignes, self.nb_colonnes), dtype=int)

        
    def __str__(self):
        return str(self.grille_visible)
    
    def calcul_position_mines(self):
        """
        Calcule la position des mines dans la grille de jeu
        """
        for i in range(self.nb_mines):
            x = rd.randint(0, self.nb_lignes-1)
            y = rd.randint(0, self.nb_colonnes-1)
            
            if [x,y] not in self.position_mines :
                self.position_mines.append([x,y])
                self.grille_numeros[x,y]=9
          
            else : 
                i -=1 #ou mettre un while à la place du for
    
    def calcul_cases_numero(self):

        for mine in self.position_mines :
            x = mine[0]
            y = mine[1]
            
            try :
                self.grille_numeros[x+1, y]+=1 #à droite de la mine
            except IndexError:
                pass
            
            try :
                self.grille_numeros[x-1, y]+=1 #à gauche de la mine
            except IndexError:
                pass
            
            try:
                #pour la ligne au dessus de la mine
                self.grille_numeros[x-1, y-1]+=1 
                self.grille_numeros[x, y-1]+=1
                self.grille_numeros[x+1, y-1]+=1
            except IndexError:
                pass
            
            try :
                #pour la grille au dessous de la mine
                self.grille_numeros[x-1, y+1]+=1
                self.grille_numeros[x, y+1]+=1
                self.grille_numeros[x+1, y+1]+=1
            except IndexError : 
                pass
        
        #pour avoir une grille propre
        for mine in self.position_mines :
            self.grille_numeros[mine[0], mine[1]]=9
            
    # def creuser(self, ligne, colonne):
    #     self.grille_visible[ligne, colonne]= str(self.grille_numeros[ligne, colonne])
    
    def creuser(self, ligne, colonne):
        numero_creuse = self.grille_numeros[ligne, colonne]
        if numero_creuse == 9:
            return True #j'ai perdu
        else :    
            self.grille_visible[ligne, colonne]= str(numero_creuse)
            return False
    
    def signaler(self, ligne, colonne):
        self.grille_visible[ligne, colonne]= '!'
    
    def designaler(self, ligne, colonne):
        self.grille_visible[ligne, colonne]= 'X'
    
        
        
    
            


#if __name__=='__main__':
    
    #test constructeurs
    # grille1 = Grille(10, 6, 4)
    # print("Test initialisation des constructeurs :\n")
    # print("Résultat attendu : 10 6 4")
    # print("Résultat obtenu  :",grille1.nb_lignes, grille1.nb_colonnes, grille1.nb_mines)
    
    # print(grille1)