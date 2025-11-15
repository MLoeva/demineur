# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 16:25:58 2025

@author: loeva
"""
import numpy as np
import random as rd

class Grille(object):
    
    def __init__(self, nb_lignes, nb_colonnes, nb_mines):
        """
        Initialise une nouvelle instance du jeu de démineur.
        
        Paramètres
        ----------
        nb_lignes : int
            Nombre de lignes de la grille.
        nb_colonnes : int
            Nombre de colonnes de la grille.
        nb_mines : int
            Nombre total de mines à placer dans la grille.
    
        Description
        -----------
        - Création de la grille visible par le joueur, remplie de 'X' (cases non révélées).
        - Initialisation de la liste des positions de mines (qui sera remplie plus tard).
        - Création de la grille contenant les indices de présence des bombes (initialisée avec des zéros, remplie plus tard)
        """
        
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
        Calcule aléatoirement la position des mines dans la grille.
        """
        mines_placees = 0

        while mines_placees < self.nb_mines:
            x = rd.randint(0, self.nb_lignes - 1)
            y = rd.randint(0, self.nb_colonnes - 1)
    
            if [x, y] not in self.position_mines:
                self.position_mines.append([x, y])
                self.grille_numeros[x, y] = 9
                mines_placees += 1
    
    def calcul_cases_numero(self):
        """
        Calcule le nombre de bombes au voisinage de chaque case de la grille.
        """
        
        for mine in self.position_mines :
            x = mine[0]
            y = mine[1]
            
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx==0 and dy==0:
                        continue
                    
                    if -1<x+dx<self.nb_lignes and -1<y+dy<self.nb_colonnes:
                        self.grille_numeros[x+dx, y+dy]+=1
   
        #pour avoir une grille_numeros propre, avec seulement des numéros de 0 à 9, car si 2 bombes voisines, elle prennent la valeur 10.
        for mine in self.position_mines :
            self.grille_numeros[mine[0], mine[1]]=9
 

    def creuser(self, ligne, colonne):
        """
        Révèle le numéro caché sous la case cliquée.
        
        Paramètres
        ----------
        ligne : int
            Ligne de la case cliquée.
        colonne : int
            Colonne de la case cliquée.
    
    
        Description
        -----------
        Lorsque le joueur clique sur une case de la grille visible (qui contient 'X'),
        cette fonction :
            - lit la valeur réelle correspondante dans `grille_numeros`,
            - met à jour `grille_visible` pour afficher cette valeur,
            - déclenche éventuellement le creusement automatique des cases voisines
              si cette valeur est un 0,
            - détecte si le joueur a cliqué sur une mine.
    
        Retour
        ------
        bool
            True  -> le joueur a cliqué sur une mine (valeur 9) et perd.
            False -> la case est révélée, et le jeu continue.
        """
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
        """

         Révèle automatiquement les cases autour d’une case valant 0.
        
            Paramètres
            ----------
            ligne : int
                Ligne de la case révélée initialement.
            colonne : int
                Colonne de la case révélée initialement.

        """
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
        """
        Marque une case comme suspectée d'être une mine par un '!'.

        Paramètres
        ----------
        ligne : int
            Ligne de la case que le joueur souhaite signaler.
        colonne : int
            Colonne de la case que le joueur souhaite signaler.
        """
        
        self.grille_visible[ligne, colonne]= '!'
    
    def designaler(self, ligne, colonne):
        """
        Dé-marque, désignalise une case qui a été marquée par un '!'

        Paramètres
        ----------
        ligne : int
            Ligne de la case que le joueur souhaite désignaler.
        colonne : int
            Colonne de la case que le joueur souhaite désignaler.
        """
        
        self.grille_visible[ligne, colonne]= 'X'
    
        
        
    
            


#if __name__=='__main__':
    
    #test constructeurs
    # grille1 = Grille(10, 6, 4)
    # print("Test initialisation des constructeurs :\n")
    # print("Résultat attendu : 10 6 4")
    # print("Résultat obtenu  :",grille1.nb_lignes, grille1.nb_colonnes, grille1.nb_mines)
    
    # print(grille1)