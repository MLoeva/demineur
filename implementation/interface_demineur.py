# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 12:03:56 2025

@author: loeva
"""


from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QComboBox, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
import sys
from partie import Partie

class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Jeu Demineur")# on donne un titre à la fenêtre
        self.resize(600,600)# on fixe la taille de la fenêtre
        self.move(600,10)# on fixe la position de la fenêtre
        
        
        self.titre = QLabel('Jeu Démineur')
        
        self.b_start = QPushButton('PushButton')
        self.b_start.clicked.connect(self.action_bouton)
        
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
        
    def afficher_message_fin(self, message):
        msg_fin = QMessageBox()
        msg_fin.setWindowTitle('FIN DE LA PARTIE')
        msg_fin.setText(message)
        msg_fin.setIcon(QMessageBox.Information)
        msg_fin.setStandardButtons(QMessageBox.Ok)
        msg_fin.exec_()
    
        
    def action_bouton(self):
        print("Le bouton a été cliqué !")
        
    
    def selectionNiveau(self, index):
        cindex = self.cb_niveau.currentIndex()
        # ctext = self.cb_niveau.itemText(index)
        # print(f"currentIndex {cindex}, text {ctext}")
        self.partie_en_cours = Partie(cindex+1)
        print(f"Niveau choisi : {cindex+1}")
        
        self.partie_en_cours.initialiserGrille()
        lignes = self.partie_en_cours.grille_jeu.nb_lignes
        colonnes = self.partie_en_cours.grille_jeu.nb_colonnes
        self.creation_tableau(lignes, colonnes)
             

    def creation_tableau(self, nb_lignes, nb_colonnes):
        self.table.setRowCount(nb_lignes)
        self.table.setColumnCount(nb_colonnes)
        for i in range(nb_colonnes):
            self.table.resizeColumnToContents(i)  
        
        for i in range(nb_lignes):
            for j in range(nb_colonnes):
                item = self.partie_en_cours.grille_jeu.grille_visible[i,j]
                self.table.setItem(i , j , QTableWidgetItem(item))
                
    def cellule_cliquee(self, ligne, colonne):
        print(f"Case cliquée : ligne {ligne}, colonne {colonne}")
        action = self.action
        
        if action == 'C':
            resultat = self.partie_en_cours.creuser_case(ligne, colonne)
            if resultat == True : #j'ai perdu
                print('iciiiiiii')
                message = 'Oh oh, tu viens de tout faire exploser..'
                self.afficher_message_fin(message)
                #self.affiche_grille_fin()
            
        elif action == 'S':
            self.partie_en_cours.signaler_case(ligne, colonne)
        elif action == 'D':
            self.partie_en_cours.designaler_case(ligne, colonne)
        
        if sum(sum(self.partie_en_cours.grille_jeu.grille_visible == 'X')) == 0:
            message = "Woaw mais t'es trop une star, quel talent incroyable !!"
            self.afficher_message_fin(message)
                        

        self.afficher_grille()

    def afficher_grille(self):
        nb_lignes = self.partie_en_cours.grille_jeu.nb_lignes
        nb_colonnes = self.partie_en_cours.grille_jeu.nb_colonnes
        for i in range(nb_lignes):
            for j in range(nb_colonnes):
                item = self.partie_en_cours.grille_jeu.grille_visible[i,j]
                self.table.setItem(i , j , QTableWidgetItem(item))
                
    #def affiche_grille_fin(self): #ne s'affiche pas
        # nb_lignes = self.partie_en_cours.grille_jeu.nb_lignes
        # nb_colonnes = self.partie_en_cours.grille_jeu.nb_colonnes
        # for i in range(nb_lignes):
        #     for j in range(nb_colonnes):
        #         item = self.partie_en_cours.grille_jeu.grille_numeros[i,j]
        #         self.table.setItem(i , j , QTableWidgetItem(item))
        
    def choix_action(self):
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
    #app.setStyle('Windows')
    if not app:
        app = QApplication(sys.argv)
        

    fen = Fenetre()
    fen.show()

    app.exec_()
