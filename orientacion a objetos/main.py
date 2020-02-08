#!/usr/local/bin/python3
#coding:utf-8

#del archivo X importamos la clase X como etiqueta X
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

#Clases propias
from Persona import persona as Persona
from Maestro import maestro as Maestro

@pyqtSlot()
def crearPersona(self):
	print("click")
def salir():
	exit()

if(__name__ == '__main__'):
	raiz = QApplication(sys.argv)
	ventana = QWidget()
	ventana.setGeometry(0, 0, 500, 300)
	ventana.setWindowTitle("Gestor de Personas")
	
	btnCrearPersona = QPushButton("CrearPersona", ventana)
	btnCrearPersona.setToolTip("interfaz para crear persona")
	btnCrearPersona.move(0,0)
	btnCrearPersona.clicked.connect(crearPersona)
	
	btnSalir = QPushButton("Salir", ventana)
	btnSalir.setToolTip("salir del programa")
	btnSalir.move(0, 35)
	btnSalir.clicked.connect(salir)
	
	ventana.show()
	sys.exit(raiz.exec())
