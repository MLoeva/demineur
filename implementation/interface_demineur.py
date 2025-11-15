# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 12:03:56 2025

@author: loeva
"""


from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QComboBox, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QDialog
from PyQt5.QtGui import QColor, QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt
import sys
from partie import Partie

class Fenetre(QWidget):
    def __init__(self):

        """
        Classe représentant l'interface graphique du jeu Démineur.
     
        Description
        -----------
        Cette classe utilise PyQt5 pour créer la fenêtre principale du jeu, 
        avec les composants suivants :
            - un titre,
            - un bouton pour afficher la solution,
            - un choix du niveau (ComboBox),
            - des boutons radio pour sélectionner l'action (Creuser, Signaler, Designaler),
            - une grille de jeu (QTableWidget) pour interagir avec les cases.

        """
        
        QWidget.__init__(self)
        self.setWindowTitle("Jeu Demineur")# on donne un titre à la fenêtre
        self.setWindowIcon(QIcon("images_interface_graphique/mine.jpg"))
        self.resize(600,600)# on fixe la taille de la fenêtre
        self.move(600,10)# on fixe la position de la fenêtre
        
        
        self.titre = QLabel('Jeu Démineur')
        self.titre.setFont(QFont('Ocr a extended', 18))
        
        self.b_start = QPushButton('Afficher la solution')
        self.b_start.clicked.connect(self.affiche_solution)
        
        self.cb_niveau = QComboBox()
        self.cb_niveau .addItem("Niveau 1")
        self.cb_niveau .addItem("Niveau 2")
        self.cb_niveau .addItem("Niveau 3")
        self.cb_niveau.activated.connect(self.selectionNiveau)
        
        self.rb_creuser = QRadioButton('Creuser')
        self.rb_signaler = QRadioButton('Signaler')
        self.rb_designaler = QRadioButton('Designaler')
        
        self.rb_creuser.toggled.connect(self.choix_action)
        self.rb_signaler.toggled.connect(self.choix_action)
        self.rb_designaler.toggled.connect(self.choix_action)
        
        self.table = QTableWidget()
        self.table.setEditTriggers(QTableWidget.NoEditTriggers) #pour bloquer l'édition des valeurs dans l'interface
        self.table.cellClicked.connect(self.cellule_cliquee)

        
        
        #layout
        layout1 = QVBoxLayout()
        layout1.addWidget(self.titre)
        
        layout2 = QHBoxLayout()
        layout2.addWidget(self.cb_niveau)
        layout2.addWidget(self.b_start)
        
        layout3 = QHBoxLayout()
        layout3.addWidget(self.rb_creuser)
        layout3.addWidget(self.rb_signaler)
        layout3.addWidget(self.rb_designaler)
        
        layout4 = QVBoxLayout()
        layout4.addWidget(self.table)
        
        layoutGeneral = QVBoxLayout()
        layoutGeneral.addLayout(layout1)
        layoutGeneral.addLayout(layout2)
        layoutGeneral.addLayout(layout3)
        layoutGeneral.addLayout(layout4)
        
        self.setLayout(layoutGeneral)
        
    def afficher_message_fin(self, message, pth_image):
        """
        Affiche une boîte de dialogue pour signaler la fin de la partie.
    
        Paramètres
        ----------
        message : str
            Le texte à afficher dans la boîte de dialogue.
        pth_image : str
            Chemin vers l'image à afficher dans la boîte de dialogue.
        """
        
        msg_fin = QMessageBox()
        msg_fin.setWindowTitle('FIN DE LA PARTIE')
        msg_fin.setText(message)
        msg_fin.setIcon(QMessageBox.Information)
        
        image = QPixmap(pth_image)
        image = image.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        msg_fin.setIconPixmap(QPixmap(image))
        msg_fin.exec_()
    
    def selectionNiveau(self, index):
        """
        Sélectionne le niveau de difficulté choisi dans la ComboBox
        et initialise une nouvelle partie.
    
        Paramètres
        ----------
        index : int
            Index de l'élément sélectionné dans le ComboBox.
            (0 pour Niveau 1, 1 pour Niveau 2, 2 pour Niveau 3)
        """
        
        cindex = self.cb_niveau.currentIndex()
        self.partie_en_cours = Partie(cindex+1)
        print(f"Niveau choisi : {cindex+1}")
        
        self.partie_en_cours.initialiserGrille()
        lignes = self.partie_en_cours.grille_jeu.nb_lignes
        colonnes = self.partie_en_cours.grille_jeu.nb_colonnes
        self.creation_tableau(lignes, colonnes)
             

    def creation_tableau(self, nb_lignes, nb_colonnes):
        """
        Crée et remplit le tableau QTableWidget correspondant à la grille de jeu.
    
        Paramètres
        ----------
        nb_lignes : int
            Nombre de lignes de la grille.
        nb_colonnes : int
            Nombre de colonnes de la grille.
        """
        
        self.table.setRowCount(nb_lignes)
        self.table.setColumnCount(nb_colonnes)
        for i in range(nb_colonnes):
            self.table.resizeColumnToContents(i)  
        
        for i in range(nb_lignes):
            for j in range(nb_colonnes):
                item = self.partie_en_cours.grille_jeu.grille_visible[i,j]
                self.table.setItem(i , j , QTableWidgetItem(item))
                
    def cellule_cliquee(self, ligne, colonne):
        """
        Gère l'action du joueur lorsqu'il clique sur une cellule de la grille.
    
        Paramètres
        ----------
        ligne : int
            Index de la ligne de la cellule cliquée.
        colonne : int
            Index de la colonne de la cellule cliquée.
        """
        
        #print(f"Case cliquée : ligne {ligne}, colonne {colonne}")
        action = self.action
        
        if action == 'C':
            resultat = self.partie_en_cours.creuser_case(ligne, colonne)
            if resultat == True : #j'ai perdu
                message = 'Oh oh, tu viens de tout faire exploser..'
                self.afficher_message_fin(message, 'images_interface_graphique/boom.jpg')
                
        elif action == 'S':
            self.partie_en_cours.signaler_case(ligne, colonne)
        elif action == 'D':
            self.partie_en_cours.designaler_case(ligne, colonne)
        
        if sum(sum(self.partie_en_cours.grille_jeu.grille_visible == 'X')) == 0:
            message = "Woaw mais t'es trop une star, quel talent incroyable !!"
            self.afficher_message_fin(message, 'images_interface_graphique/bravo.png')
                        

        self.afficher_grille()

    def afficher_grille(self):
        """
        Met à jour l'affichage de la grille dans le QTableWidget avec les couleurs 
        correspondant aux valeurs de chaque case.
        """
        nb_lignes = self.partie_en_cours.grille_jeu.nb_lignes
        nb_colonnes = self.partie_en_cours.grille_jeu.nb_colonnes
        for i in range(nb_lignes):
            for j in range(nb_colonnes):
                item = self.partie_en_cours.grille_jeu.grille_visible[i,j]
                cellule =  QTableWidgetItem(item)
                self.table.setItem(i , j ,cellule)
                
                if item == '0' :
                    cellule.setBackground(QColor(200, 230, 200))
                    
                if item == '1' :
                    cellule.setBackground(QColor(200, 255, 200))  # vert clair
                
                if item == '2' :
                    cellule.setBackground(QColor(255, 255, 0))  # jaune
                    
                if item == '3' :
                    cellule.setBackground(QColor(255, 100, 0))  # orange
                
                if item == '4' or item == '5' or item == '6' or item == '7' or item == '8' :
                    cellule.setBackground(QColor(255, 0, 0)) #rouge
                
                if item == '!':
                    cellule.setBackground(QColor(160, 0, 160))
    
    def affiche_solution(self):
        """
        Affiche la solution complète de la grille en révélant toutes les cases
        (les numéros et les mines)(grille_numeros).
        """
        nb_lignes = self.partie_en_cours.grille_jeu.nb_lignes
        nb_colonnes = self.partie_en_cours.grille_jeu.nb_colonnes
        for i in range(nb_lignes):
            for j in range(nb_colonnes):
                item = str(self.partie_en_cours.grille_jeu.grille_numeros[i,j])
                cellule =  QTableWidgetItem(item)
                self.table.setItem(i , j ,cellule)
                
                if item == '0' :
                    cellule.setBackground(QColor(200, 230, 200))
                    
                if item == '1' :
                    cellule.setBackground(QColor(200, 255, 200))  # vert clair
                
                if item == '2' :
                    cellule.setBackground(QColor(255, 255, 0))  # jaune
                    
                if item == '3' :
                    cellule.setBackground(QColor(255, 100, 0))  # orange
                
                if item == '4' :
                    cellule.setBackground(QColor(255, 0, 0)) #rouge
                    
                if item == '9' :
                    cellule.setBackground(QColor(10, 10, 10)) #rouge
                
                if item == '!':
                    cellule.setBackground(QColor(160, 0, 160))
                    
        
    def choix_action(self):
        """
        Met à jour l'action du joueur selon le bouton radio sélectionné.
    
        Description
        -----------
        Cette méthode est connectée aux boutons radio (`rb_creuser`, `rb_signaler`,
        `rb_designaler`). Elle est appelée automatiquement lorsque l'utilisateur
        sélectionne un bouton radio.
        """
        
        # get the radio button the send the signal
        rb = self.sender()

        # check if the radio button is checked
        if rb.isChecked():
            print('bouton selectioné :', rb.text())
            #self.result_label.setText(f'You selected {rb.text()}')
            self.action = rb.text().upper()[0]
            print('action : ', self.action)
        
        

if __name__ == "__main__":
    
    app = QApplication.instance() 
    #app.setStyle('Fusion')
    if not app:
        app = QApplication(sys.argv)
        

    fen = Fenetre()
    fen.show()

    app.exec_()
