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
            

    def creuser(self, ligne, colonne):
        numero_creuse = self.grille_numeros[ligne-1, colonne-1]
        if numero_creuse == 9:
            return True #j'ai perdu
        
        if numero_creuse == 0:
            self.grille_visible[ligne-1, colonne-1]= str(numero_creuse)

            for i in range(-2, 1, 1):
                for j in range(-2, 1, 1):
                    try :
                        if self.grille_numeros[ligne+i, colonne+j]!=9:
                            self.grille_visible[ligne+i, colonne+j]= str(self.grille_numeros[ligne+i, colonne+j])
                        
                    except IndexError : 
                        pass                
            return False
        
        else :    
            self.grille_visible[ligne-1, colonne-1]= str(numero_creuse)
            return False
    
    # def creuser(self, ligne, colonne):
    #     numero_creuse = self.grille_numeros[ligne-1, colonne-1]
    #     if numero_creuse == 9:
    #         return True #j'ai perdu
        
    #     if numero_creuse == 0:
    #         self.grille_visible[ligne-1, colonne-1]= str(numero_creuse)
    #         regarder_autour_de = self.creuse_autour(ligne,colonne)
    #         print(regarder_autour_de)
    #         for i in range(len(regarder_autour_de)):
    #             ligne = regarder_autour_de[i][0]
    #             colonne=regarder_autour_de[i][1]
    #             self.creuse_autour(ligne-1,colonne-1)
    #         return False
        
    #     else :    
    #         self.grille_visible[ligne-1, colonne-1]= str(numero_creuse)
    #         return False
    
    # def creuse_autour(self, ligne, colonne):
    #     regarder_autour_de =[]
    #     for i in range(-2, 1, 1):
    #         for j in range(-2, 1, 1):
    #             numero = self.grille_numeros[ligne+i, colonne+j]
    #             try :
    #                 if numero!=9:
    #                     if numero==0:
    #                         regarder_autour_de.append([ligne+i,colonne+j])
                            
    #                     self.grille_visible[ligne+i, colonne+j]= str(numero)
                    
    #             except IndexError : 
    #                 pass 
    #     return regarder_autour_de
        
    
    def signaler(self, ligne, colonne):
        self.grille_visible[ligne-1, colonne-1]= '!'
    
    def designaler(self, ligne, colonne):
        self.grille_visible[ligne-1, colonne-1]= 'X'
    
        
        
    
            


#if __name__=='__main__':
    
    #test constructeurs
    # grille1 = Grille(10, 6, 4)
    # print("Test initialisation des constructeurs :\n")
    # print("Résultat attendu : 10 6 4")
    # print("Résultat obtenu  :",grille1.nb_lignes, grille1.nb_colonnes, grille1.nb_mines)
    
    # print(grille1)