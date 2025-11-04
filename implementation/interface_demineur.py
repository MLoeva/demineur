# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 12:03:56 2025

@author: loeva
"""


from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QComboBox, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem
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
        
        self.rb_creuser.toggled.connect(self.update)
        self.rb_signaler.toggled.connect(self.update)
        self.rb_designaler.toggled.connect(self.update)
        
        self.table = QTableWidget()
        
        
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
                self.table.setItem(i , j , QTableWidgetItem('X'))
                
        
    def update(self):
        # get the radio button the send the signal
        rb = self.sender()

        # check if the radio button is checked
        if rb.isChecked():
            print('bouton selectioné :', rb.text())
            #self.result_label.setText(f'You selected {rb.text()}')
    
        
        

if __name__ == "__main__":
    
    app = QApplication.instance() 
    app.setStyle('Fusion')
    if not app:
        app = QApplication(sys.argv)
        

    fen = Fenetre()
    fen.show()

    app.exec_()
