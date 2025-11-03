# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 18:54:28 2025

@author: loeva
"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel, QLineEdit
import sys

app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
    
fenetre = uic.loadUi( "test_qtdesigner.ui" )
fenetre.show()

app.exec_()