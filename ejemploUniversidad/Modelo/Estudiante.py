#!usr/bin/python3

from Persona import Persona

class Estudiante(Persona):
	
	CreditosDelClicloLectivo = 0
	CreditosAprobados = 0
	PromedioGeneral = 0.0
	Estado = 0
	
	def __init__(self, dni, primerNombre, segundoNombre = None, primerApellido, segundoApellido, fechaDeNacimiento, creditosDelClicloLectivo, creditosAprobados, promedioGeneral, Estado):
		super(dni, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaDeNacimiento)
		
		
	def setCreditosDelCicloLectivo(self, creditosDelClicloLectivo):
		self.CreditosDelClicloLectivo = creditosDelCicloLectivo
	
	def getCreditosDelClicloLectivo(self):
		return self.CreditosDelClicloLectivo
		
	def setCreditosAprobados(self, creditosAprobados):
		self.CreditosAprobados = creditosAprobados
		
	def getCreditosAprobados(self):
		return self.CreditosAprobados
		
	def setPromedioGeneral(self, promedioGeneral):
		self.PromedioGeneral = promedioGeneral
		
	def getPromedioGeneral(self):
		return self.PromedioGeneral
		
	def setEstado(self, estado):
		self.Estado = estado
		
	def getEstado(self):
		return self.Estado

