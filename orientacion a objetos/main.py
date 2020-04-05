#!/usr/local/bin/python3
#coding:utf-8

#Importando las clases de interfaz
import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QDialog, QLineEdit, 
								QPushButton, QVBoxLayout, QLabel)

#Clases propias
from Persona import persona as Persona
from Maestro import maestro as Maestro

raiz = 0 #variableGlobal

class ventanaPrincipal(QDialog):
	def __init__(self, parent = None):
		super(ventanaPrincipal, self).__init__(parent)
		raiz.setWindowTitle("Ventana Principal")
		self.instanciarVentanaPrincipal()
	
	def instanciarVentanaPrincipal(self):
		
		#componentes de la ventana
		self.btnCrearPersona = QPushButton("Crear Persona")
		self.btnCrearMaestro = QPushButton("Crear Maestro")
		self.btnSalir = QPushButton("Salir")
		
		#controlador de la ventana
		layout = QVBoxLayout()
		layout.addWidget(self.btnCrearPersona)
		layout.addWidget(self.btnCrearMaestro)
		layout.addWidget(self.btnSalir)
		
		#añadir el controlador de ventana
		self.setLayout(layout)
		
		#añadir la señal hacia el botón
		self.btnCrearPersona.clicked.connect(self.crearPersona)
		self.btnCrearMaestro.clicked.connect(self.crearMaestro)
		self.btnSalir.clicked.connect(self.salir)
	
	def crearPersona(self):
		raiz.setCentralWidget(None)
		raiz.setCentralWidget(creacionDePersonas())
	
	def crearMaestro(self):
		raiz.setCentralWidget(None)
		raiz.setCentralWidget(creacionDeMaestros())
		
	
	def salir(self):
		QApplication.quit()
	
class creacionDeMaestros(QDialog):
	def __init__(self, parent = None):
		super(creacionDeMaestros, self).__init__(parent)
		raiz.setWindowTitle("Crear Maestros")
		self.instanciarMaestros()
	
	def instanciarMaestros(self):
		#etiquetas
		lblNombre = QLabel("Nombre: ")
		lblApellido = QLabel("Apellido: ")
		lblEdad = QLabel("Edad: ")
		lblMateria = QLabel("Materia: ")
		#campos de texto
		self.txtNombre = QLineEdit()
		self.txtApellido = QLineEdit()
		self.txtEdad = QLineEdit()
		self.txtMateria = QLineEdit()
		#botones
		btnAceptar = QPushButton("Aceptar")
		btnCancelar = QPushButton("Cancelar")
		#controlador de la ventana
		layout = QVBoxLayout()
		
		layout.addWidget(lblNombre)
		layout.addWidget(self.txtNombre)
		
		layout.addWidget(lblApellido)
		layout.addWidget(self.txtApellido)
		
		layout.addWidget(lblEdad)
		layout.addWidget(self.txtEdad)
		
		layout.addWidget(lblMateria)
		layout.addWidget(self.txtMateria)
		
		layout.addWidget(btnAceptar)
		layout.addWidget(btnCancelar)
		
		#agregar al controlador de la ventana
		self.setLayout(layout)
		
		#eventos
		btnAceptar.clicked.connect(self.aceptar)
		btnCancelar.clicked.connect(self.cancelar)
		
	def aceptar(self):
		nuevoMaestro = Maestro(self.txtNombre.text(), self.txtApellido.text(), 
		self.txtEdad.text(), self.txtMateria.text())
		self.cancelar()

	def cancelar(self):
		raiz.setCentralWidget(None)
		raiz.setCentralWidget(ventanaPrincipal())
		
class creacionDePersonas(QDialog):
	
	def __init__(self, parent = None):
		super(creacionDePersonas, self).__init__(parent)
		raiz.setWindowTitle("Crear Persona")
		self.instanciarPersonas()
	
	def instanciarPersonas(self):
		#etiquetas
		lblNombre = QLabel("Nombre: ")
		lblApellido = QLabel("Apellido: ")
		lblEdad = QLabel("Edad: ")
		
		#campos de texto
		self.txtNombre = QLineEdit()
		self.txtApellido = QLineEdit()
		self.txtEdad = QLineEdit()
		
		#botones
		btnAceptar = QPushButton("Aceptar")
		btnCancelar = QPushButton("Cancelar")
		
		#controlador de la ventana
		layout = QVBoxLayout()
		layout.addWidget(lblNombre)
		layout.addWidget(self.txtNombre)
		
		layout.addWidget(lblApellido)
		layout.addWidget(self.txtApellido)
		
		layout.addWidget(lblEdad)
		layout.addWidget(self.txtEdad)
		
		layout.addWidget(btnAceptar)
		layout.addWidget(btnCancelar)
		
		#agregar al controlador de la ventana
		self.setLayout(layout)
		
		#Eventos
		btnAceptar.clicked.connect(self.aceptar)
		btnCancelar.clicked.connect(self.cancelar)
		
	def aceptar(self):
		nuevaPersona = Persona(self.txtNombre.text(), self.txtApellido.text(), self.txtEdad.text())
		self.cancelar()
		
	def cancelar(self):
		raiz.setCentralWidget(None)
		raiz.setCentralWidget(ventanaPrincipal())
	

if __name__== '__main__':
	app = QApplication(sys.argv)
	raiz = QMainWindow()
	raiz.setCentralWidget(ventanaPrincipal())
	raiz.show()
	sys.exit(app.exec_())
	
