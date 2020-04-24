#!/usr/bin/python3

import sys
from PySide2.QtWidgets import(QApplication, QMainWindow, QFrame, QPlainTextEdit,
QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QDateEdit, QMessageBox)

from datetime import date
#se sube un nivel en el arbol de archivos para importar el contenido de
#las carpetas de niveles inferiores
sys.path.append("../")

#Inicio clases Propias
from Modelo.Persona import Persona
from Controlador.OperacionesConPersonas import OperacionesConPersonas
#Fin clases propias


app = 0#variable global que contiene QApplication
raiz = 0#variable global que contiene a QMainWindow

class VentanaPrincipal(QFrame):
	def __init__(self, parent = None):
		super(VentanaPrincipal, self).__init__(parent)
		raiz.setWindowTitle("Ventana Principal")
		
		self.instanciarVentana()
	
	def instanciarVentana(self):
		layout = QVBoxLayout()
		
		self.btnAdministrarPersonas = QPushButton("Administrar personas")
		self.btnAdministrarPersonas.clicked.connect(self.cambiarVentanaPersonas)
		layout.addWidget(self.btnAdministrarPersonas)
		
		self.btnSalir = QPushButton("Cerrar")
		self.btnSalir.clicked.connect(self.salir)
		layout.addWidget(self.btnSalir)
		
		self.setLayout(layout)
		
		#Redimensionar
		raiz.adjustSize()
		self.adjustSize()
		
	def cambiarVentanaPersonas(self):
		raiz.setCentralWidget(None)
		raiz.setCentralWidget(VentanaAdministradorDePersonas())
		
	def salir(self):
		app.quit()
	
class VentanaAdministradorDePersonas(QFrame):
	
	def __init__(self, parent = None):
		super(VentanaAdministradorDePersonas, self).__init__(parent)
		raiz.setWindowTitle("Administracion de personas")
		self.operacionesConPersonas = OperacionesConPersonas()
		self.instanciarVentana()
		
	def instanciarVentana(self):
		#Contenedor De todas las cosas de arriba a abajo
		layoutGeneral = QVBoxLayout()
		
		#Cosas de Derecha
		layoutDerecha = QVBoxLayout()#Ordena cosas de arriba a abajo
		layoutDerecha.setMargin(20)
		
		self.btnAgregarPersona = QPushButton("Agregar persona")
		self.btnAgregarPersona.setToolTip("Toma los datos ")
		self.btnAgregarPersona.clicked.connect(self.agregarPersona)
		layoutDerecha.addWidget(self.btnAgregarPersona)
		
		self.btnBuscarPersona = QPushButton("Buscar persona")
		self.btnBuscarPersona.setToolTip("Busca por cedula a una persona")
		self.btnBuscarPersona.clicked.connect(self.buscarPersona)
		layoutDerecha.addWidget(self.btnBuscarPersona)
		
		self.btnEliminarPersona = QPushButton("Eliminar persona")
		self.btnEliminarPersona.setToolTip("Elimina a la persona que esta en busqueda")
		self.btnEliminarPersona.clicked.connect(self.eliminarPersona)
		layoutDerecha.addWidget(self.btnEliminarPersona)
		
		self.btnActualizarPersona  = QPushButton("Actualizar persona")
		self.btnActualizarPersona.setToolTip("Cambia los datos de la persona seleccionada")
		self.btnActualizarPersona.clicked.connect(self.actualizarPersona)
		layoutDerecha.addWidget(self.btnActualizarPersona)
		
		self.btnLimpiarTexto = QPushButton("Limpiar")
		self.btnLimpiarTexto.setToolTip("Limpia los campos de texto para ingresar datos")
		self.btnLimpiarTexto.clicked.connect(self.limpiarCampos)
		layoutDerecha.addWidget(self.btnLimpiarTexto)
		
		self.btnVolverAlMenu = QPushButton("Volver")
		self.btnVolverAlMenu.setToolTip("Vuelve al menu principal")
		self.btnVolverAlMenu.clicked.connect(self.volverAlMenu)
		layoutDerecha.addWidget(self.btnVolverAlMenu)
		
		
		
		#Cosas de Izquierda
		layoutIzquierda = QVBoxLayout()#ordena cosas de arriba a abajo
		
		self.lblDNI = QLabel("DNI: ")
		layoutIzquierda.addWidget(self.lblDNI)
		self.DNI = QLineEdit()
		layoutIzquierda.addWidget(self.DNI)
		
		self.lblPrimerNombre = QLabel("Primer nombre: ")
		layoutIzquierda.addWidget(self.lblPrimerNombre)
		self.PrimerNombre = QLineEdit()
		layoutIzquierda.addWidget(self.PrimerNombre)
		
		self.lblSegundoNombre = QLabel("Segundo nombre: ")
		layoutIzquierda.addWidget(self.lblSegundoNombre)
		self.SegundoNombre = QLineEdit()
		layoutIzquierda.addWidget(self.SegundoNombre)
		
		self.lblPrimerApellido = QLabel("Primer apellido: ")
		layoutIzquierda.addWidget(self.lblPrimerApellido)
		self.PrimerApellido = QLineEdit()
		layoutIzquierda.addWidget(self.PrimerApellido)
		
		self.lblSegundoApellido = QLabel("Segundo apellido: ")
		layoutIzquierda.addWidget(self.lblSegundoApellido)
		self.SegundoApellido = QLineEdit()
		layoutIzquierda.addWidget(self.SegundoApellido)
		
		self.lblFechaDeNacimiento = QLabel("Fecha de nacimiento")
		layoutIzquierda.addWidget(self.lblFechaDeNacimiento)
		self.fechaDeNacimiento = QDateEdit()
		self.fechaDeNacimiento.setDisplayFormat("yyyy-MM-dd")
		self.fechaDeNacimiento.setCalendarPopup(True)
		self.fechaDeNacimiento.setDate(date.today())
		layoutIzquierda.addWidget(self.fechaDeNacimiento)
		
		
		#Cosas de layout de arriba
		layoutSuperior = QHBoxLayout()#Ordena cosas de derecha a izquierda
		layoutSuperior.addLayout(layoutIzquierda)
		layoutSuperior.addLayout(layoutDerecha)
		
		#Cosas layout de abajo
		layoutInferior = QVBoxLayout()
		self.mostrarError = QPlainTextEdit(readOnly= True)
		layoutInferior.addWidget(self.mostrarError)
		
		
		#cosas del layout general
		layoutGeneral.addLayout(layoutSuperior)
		layoutGeneral.addLayout(layoutInferior)
		self.setLayout(layoutGeneral)
		
		#Redimensionar
		raiz.adjustSize()
		self.adjustSize()
		
	def agregarPersona(self):
		self.limpiarErrores()
		try:
			laPersona = self.llenarPersona()
			salida = self.operacionesConPersonas.insertarPersona(laPersona)
			self.mostrarError.insertPlainText(str(salida))
			self.limpiarCampos()#habilitamos la edicion y evitamos dejar datos basura
		except Exception as e:
			self.mostrarError.insertPlainText(''.join(e.args))
		pass
	def buscarPersona(self):
		self.limpiarErrores()
		try:
			laPersona = self.operacionesConPersonas.buscarPersonaPorDNI(int(''.join(self.DNI.text())))
			if type(laPersona) == type(""):
				self.mostrarError.insertPlainText(''.join(laPersona))
				return None
			self.llenarCampos(laPersona)
		except Exception as e:
			self.mostrarError.insertPlainText(''.join(e.args))
				
		
		pass
	def eliminarPersona(self):
		self.limpiarErrores()
		try:
			laPersona = self.llenarPersona()
			mensajeDeConfirmacion = "DNI: "+self.DNI.text()
			opcionElegida = QMessageBox.question(self, "Desea eliminar a la persona?", mensajeDeConfirmacion, QMessageBox.Yes, QMessageBox.No)
			if opcionElegida == QMessageBox.Yes:
				respuesta = self.operacionesConPersonas.eliminarPersona(laPersona)
				if type(respuesta) == type(""):
					self.mostrarError.insertPlainText(''.join(respuesta))
					self.limpiarCampos()
					return None
				
		except Exception as e:
			self.mostrarError.insertPlainText(''.join(e.args))
		
	def actualizarPersona(self):
		self.limpiarErrores()
		try:
			
			laPersona = self.llenarPersona()
			mensajeDeConfirmacion = "DNI: "+self.DNI.text()
			opcionElegida = QMessageBox.question(self, "Desea eliminar a la persona?", mensajeDeConfirmacion, QMessageBox.Yes, QMessageBox.No)
			if opcionElegida == QMessageBox.Yes:
				respuesta = self.operacionesConPersonas.actualizarPersona(laPersona)
				if type(respuesta) == type(""):
					self.mostrarError.insertPlainText(''.join(respuesta))
					self.limpiarCampos()
					return None
		except Exception as e:
			print(e.args)
	
	def llenarCampos(self, laPersona):
		self.limpiarCampos()
		self.DNI.setText(str(laPersona.getDNI()))
		self.DNI.setReadOnly(True)
		self.PrimerNombre.setText(laPersona.getPrimerNombre())
		self.SegundoNombre.setText(laPersona.getSegundoNombre())
		self.PrimerApellido.setText(laPersona.getPrimerApellido())
		self.SegundoApellido.setText(laPersona.getSegundoApellido())
		self.fechaDeNacimiento.setDate(laPersona.getFechaDeNacimiento())
		
	def llenarPersona(self):
		return Persona(int(''.join(self.DNI.text())), ''.join(self.PrimerNombre.text()), ''.join(self.SegundoNombre.text()), ''.join(self.PrimerApellido.text()), ''.join(self.SegundoApellido.text()), ''.join(self.fechaDeNacimiento.text()))
		
	def limpiarCampos(self):
		self.DNI.clear()
		self.DNI.setReadOnly(False)
		self.PrimerNombre.clear()
		self.SegundoNombre.clear()
		self.PrimerApellido.clear()
		self.SegundoApellido.clear()
		self.fechaDeNacimiento.setDate(date.today())
		
		#limpiar campos de texto y permitir la edicion de todos ellos
		pass
	def limpiarErrores(self):
		self.mostrarError.clear()
		
	def volverAlMenu(self):
		
		raiz.setCentralWidget(None)
		raiz.setCentralWidget(VentanaPrincipal())


if __name__=='__main__':
	app = QApplication(sys.argv)
	raiz = QMainWindow()
	raiz.setCentralWidget(VentanaPrincipal())
	raiz.show()
	sys.exit(app.exec_())
