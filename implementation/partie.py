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
            self.grille_jeu = Grille(10, 10, 6)
            self.position_mines = self.grille_jeu.calcul_position_mines() #mettre self.grille_jeu et non Grille car on fait appel à l'instance
            self.grille_numeros = self.grille_jeu.calcul_cases_numero()
            
        elif self.niveau == 2:
            self.grille_jeu = Grille(15, 15, 15)
            self.position_mines = self.grille_jeu.calcul_position_mines()
            self.grille_numeros = self.grille_jeu.calcul_cases_numero()
            
        elif self.niveau == 3: 
            self.grille_jeu = Grille(20, 20, 25)
            self.position_mines = self.grille_jeu.calcul_position_mines()
            self.grille_numeros = self.grille_jeu.calcul_cases_numero()
            
        else :
            print('ERREUR Niveau indisponibles, merci de choisir entre 1, 2 ou 3 ')
            
            
    def gagner_partie(self, issue:bool):
        if issue == True :
            print("BRAVO ! Tu as gagné !")
        
        if issue == False :
            print("Oh oh.. tu viens de tout faire exploser")
        
    def jouer(self):
        
        resultat = False
        while resultat == False:
            try :
                action = input('Quelle action faire ? (creuser, signaler, designaler)')
                case = input('Sur quelle case ? (Répondre au format : ligne colonne').split()
            
                
                if action == 'creuser': 
                    resultat = self.grille_jeu.creuser(int(case[0]),int(case[1]))
                    print(self.grille_jeu)
                    #print('RESULTAT', resultat)
                    
                elif action == 'signaler' :
                    self.grille_jeu.signaler(case[0],case[1])
                    print(self.grille_jeu)
                    
                elif action== 'designaler':
                    self.grille_jeu.designaler(case[0],case[1])
                    print(self.grille_jeu)
                
                # elif 'X' not in self.grille_jeu :
                #     gagner_partie(True)
                else :
                    print('\nERREUR Veuillez choisir une action parmi : creuser, signaler, designaler\n')
        
                
                
            except IndexError : 
                print('\nERREUR Veuiller choisir une case DANS la grille\n')
                
        partie_en_cours.gagner_partie(False)

if __name__=='__main__':
    niveau = int(input('Choisi le niveau de difficulté : (1,2 ou 3)'))
    print('Voici la grille de jeu')
    partie_en_cours = Partie(niveau)
    partie_en_cours.initialiserGrille()
    print(partie_en_cours.grille_jeu)
    print(partie_en_cours.grille_jeu.grille_numeros)
    partie_en_cours.jouer()
    
    #MES TESTS
    # partie1 = Partie(1)
    # partie1.initialiserGrille()
    # partie1.jouer(False)
    
    # resultat = partie1.grille_jeu.creuser(3,3)
    # partie1.finPartie()
    # print(partie1.grille_jeu)
    
    
    
    #TESTS PROPRES
    
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