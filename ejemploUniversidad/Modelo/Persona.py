#!/usr/bin/python3
from datetime import date

class Persona():
	DNI = 0
	PrimerNombre = ""
	SegundoNombre = ""
	PrimerApellido = ""
	SegundoApellido = ""
	FechaDeNacimiento = date.today()
	#No accesar a datos directamente, aunque sea legal
	#Los casos especiales no son lo suficientemente especiales como para romper las reglas
	
	def __init__(self):
		pass#creacion sin argumentos
	def __init__(self, dni, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaDeNacimiento):
		self.setDNI(dni)
		self.setPrimerNombre(primerNombre) 
		self.setSegundoNombre(segundoNombre)
		self.setPrimerApellido(primerApellido)
		self.setSegundoApellido(segundoApellido)
		self.setFechaDeNacimiento(fechaDeNacimiento)
	
	def getDNI(self):
		return self.DNI
	
	def setDNI(self, dni):
		self.DNI = dni
	
	def getPrimerNombre(self):
		return self.PrimerNombre
		
	def setPrimerNombre(self, primerNombre):
		self.PrimerNombre = primerNombre
	
	def getSegundoNombre(self):
		return self.SegundoNombre
	
	def setSegundoNombre(self, segundoNombre):
		self.SegundoNombre = segundoNombre
	
	def getPrimerApellido():
		return self.PrimerApellido
	
	def setPrimerApellido(self, primerApellido):
		self.PrimerApellido = primerApellido
	
	def getSegundoApellido(self):
		return self.SegundoApellido
	
	def setSegundoApellido(self, segundoApellido):
		self.SegundoApellido = segundoApellido
	
	def getFechaDeNacimiento(self):
		print(type(self.FechaDeNacimiento))
		return self.FechaDeNacimiento
	
	def setFechaDeNacimiento(self, fechaDeNacimiento):
		if type(fechaDeNacimiento) == type(date):
			fecha = fechaDeNacimiento.split("-")
			self.FechaDeNacimiento = date(int(fecha[0]), int(fecha[1]), int(fecha[2]))
		elif type(fechaDeNacimiento) == type(tuple):
			self.FechaDeNacimiento = date(int(fecha[0]), int(fecha[1]), int(fecha[2]))
		else:
			self.FechaDeNacimiento = fechaDeNacimiento
	
if __name__=='__main__':
	print("No se espera que este codigo sea ejecutado sin su contexto")
