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
            
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx==0 and dy==0:
                        continue
                    
                    if 0<x+dx<self.nb_lignes and 0<y+dy<self.nb_lignes:
                        self.grille_numeros[x+dx, y+dy]+=1
                        
            
            # try :
            #     if y!=self.nb_colonnes-1:
            #         self.grille_numeros[x+1, y]+=1 #à droite de la mine
            # except IndexError:
            #     pass
            
            # try :
            #     if y!=0:
            #         self.grille_numeros[x-1, y]+=1 #à gauche de la mine #ca marche !
            # except IndexError:
            #     pass
            
            # try:
            #     #pour la ligne au dessus de la mine
            #     if x!=0:
            #         self.grille_numeros[x-1, y-1]+=1 
            #         self.grille_numeros[x, y-1]+=1
            #         self.grille_numeros[x+1, y-1]+=1
            # except IndexError:
            #     pass
            
            # try :
            #     #pour la ligne au dessous de la mine
            #     if x!=self.nb_colonnes-1:
            #         self.grille_numeros[x-1, y+1]+=1
            #         self.grille_numeros[x, y+1]+=1
            #         self.grille_numeros[x+1, y+1]+=1
            # except IndexError : 
            #     pass
        
        #pour avoir une grille propre
        for mine in self.position_mines :
            self.grille_numeros[mine[0], mine[1]]=9
            
    # def creuser(self, ligne, colonne):
    #     numero_creuse = self.grille_numeros[ligne-1, colonne-1]
    #     if numero_creuse == 9:
    #         return True #j'ai perdu
        
    #     if numero_creuse == 0:
    #         self.grille_visible[ligne-1, colonne-1]= str(numero_creuse)
    #         for i in range(-2, 1, 1):
    #             for j in range(-2, 1, 1):
    #                 try :
    #                     numero=self.grille_numeros[ligne+i, colonne+j]
    #                     if numero!=9:
    #                         self.grille_visible[ligne+i, colonne+j]= str(numero)
                        
    #                 except IndexError : 
    #                     pass                
    #         return False
        
    #     else :    
    #         self.grille_visible[ligne-1, colonne-1]= str(numero_creuse)
    #         return False


    def creuser(self, ligne, colonne):
        numero_creuse = self.grille_numeros[ligne, colonne]
        if numero_creuse == 9:
            return True #j'ai perdu
        
        if numero_creuse == 0:
            self.grille_visible[ligne, colonne]= str(numero_creuse)
            self.creuse_autour(ligne, colonne)       
            return False
        
        else :    
            self.grille_visible[ligne, colonne]= str(numero_creuse)
            return False
    
    def creuse_autour(self, ligne, colonne):
        a_creuser_autour = [[ligne, colonne]] 
        
        for case_creusee in a_creuser_autour:
            #print('à creuser autour', a_creuser_autour)
            ligne = case_creusee[0]
            colonne = case_creusee[1]
            
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if ligne ==0:
                        if i==-1:
                            i+=1
                    if colonne==0:
                        if j==-1:
                            j+=1
                    try :
                        numero=self.grille_numeros[ligne+i, colonne+j]
                        if numero!=9:
                            if numero==0 and [ligne+i, colonne+j] not in a_creuser_autour and -1<ligne+i<=self.nb_lignes and -1<colonne<=self.nb_colonnes:
                                a_creuser_autour.append([ligne+i, colonne+j])
                            self.grille_visible[ligne+i, colonne+j]= str(numero)
                        
                    except IndexError : 
                        pass
            
    
    
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