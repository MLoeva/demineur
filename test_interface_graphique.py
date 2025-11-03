# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 19:07:15 2025

@author: loeva
"""

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget

# app = QApplication.instance() 
# if not app:
#     app = QApplication(sys.argv)

# fen = QWidget()


# fen.setWindowTitle("Premiere fenetre")# on donne un titre à la fenêtre
# fen.resize(500,250)# on fixe la taille de la fenêtre
# fen.move(800,150)# on fixe la position de la fenêtre
# fen.show()

# app.exec_()


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel, QLineEdit

#pour avoir accès à des fontionnalités autres que celles dans PyQT, créer la class Fenetre
class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Ma fenetre")
        self.setWindowTitle("Premiere fenetre")# on donne un titre à la fenêtre
        self.resize(500,250)# on fixe la taille de la fenêtre
        self.move(800,150)# on fixe la position de la fenêtre
        
        #ajout de Qlabel
        self.n = 0
        self.label = QLabel("appui n = " + str(self.n))
        self.label_text_copie = QLabel("texte copié :")
        
        #ajouts de boutons
        self.bouton1 = QPushButton("mon premier bouton dans un QVBoxLayout")
        self.bouton2 = QPushButton("mon deuxieme bouton dans un QVBoxLayout")
        self.bouton_copie = QPushButton("COPIE")
        
        self.bouton1.clicked.connect(self.appui_bouton1)
        self.bouton2.clicked.connect(self.appui_bouton2)
        self.bouton_copie.clicked.connect(self.appui_bouton_copie)
        
        #ajout de cases à cocher
        self.case = QCheckBox("Voici ma premiere case a cocher")
        self.case.stateChanged.connect(self.etat_change)
        
        #ajout champs texte
        self.champ = QLineEdit("Voici mon premier champ de texte")
        
        
        # creation du gestionnaire de mise en forme
        layout = QVBoxLayout() 
        #layoutH = QHBoxLayout() 
        layout.addWidget(self.bouton1)
        layout.addWidget(self.bouton2)
        layout.addWidget(self.bouton_copie)
        layout.addWidget(self.case)
        layout.addWidget(self.label)
        layout.addWidget(self.label_text_copie)
        layout.addWidget(self.champ)
        # on fixe le gestionnaire de mise en forme de la fenetre
        self.setLayout(layout)
 
        self.setWindowTitle("Ma fenetre")
        
    
    # def mousePressEvent(self, event):
    #     print("appui souris")
    
    def mouseDoubleClickEvent(self, event):
        print('double clic souris')
        
    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            print("appui bouton gauche")
            print("position = " + str(event.x()) + " " + str(event.y()))
    
    def appui_bouton1(self):
            # on incrémente l'attribut "n" de 1
            self.n = self.n + 1 
            # on utilise la méthode "setText" de QLabel pour fixer le texte
            self.label.setText("appui n = " + str(self.n))
        
    def appui_bouton2(self):
        print("Appui sur le bouton2")
    
    def appui_bouton_copie(self):
       # la méthode "text" de QLineEdit permet d'obtenir le texte à copier
       texte_a_copier = self.champ.text()
       # la méthode "setText" de QLabel permet de changer le texte de l'étiquette
       self.label_text_copie.setText("texte copié :" + texte_a_copier)
   
        
    def etat_change(self):
        print("action sur la case")
        if self.case.checkState() == Qt.Checked:
            print("coche")
        else:
            print("decoche") 

app = QApplication.instance() 
#app.setStyle('Fusion')
if not app:
    app = QApplication(sys.argv)
    

fen = Fenetre()
fen.show()

app.exec_()