#!/usr/local/bin/python3
#coding:utf-8
from Persona import persona as Persona

class maestro(Persona):
	__persona = ""
	__materiaQueImparte = ""
	
	def __init__(self, nombre, apellido, edad, materia):
		self.__persona = Persona(nombre, apellido, edad)
		self.setMateria(materia)
		
	def setMateria(self, materia):
		self.__materiaQueImparte = materia
	
	def getMateria(self):
		return self.__materiaQueImparte
