#!usr/bin/python3

from Persona import Persona


class Maestro(Persona):
	HorasLaboradas = 0
	Estado = 0
	def __init__(self, dni, primerNombre, segundoNombre = None, primerApellido, segundoApellido, fechaDeNacimiento, horasLaboradas, estado):
		super(self, dni, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaDeNacimiento)
		self.setHorasLaboradas(horasLaboradas)
		self.setEstado(estado)
		
	def setHorasLaboradas(self, horasLaboradas):
		self.HorasLaboradas = horasLaboradas
		
	def getHorasLaboradas(self):
		return self.HorasLaboradas
		
	def setEstado(self, estado):
		self.Estado = estado
		
	def getEstado(self):
		return self.Estado
			
