#!/usr/local/bin/python3
#coding:utf-8
from Persona import persona as Persona

class maestro(Persona):
	__persona = ""
	__materiaQueImparte = ""
	
	def __init__(self, nombre, apellido, edad, materia):
		self.__persona = Persona(nombre, apellido, edad) #se guarda un objeto del tipo persona en la variable global __persona
		self.setMateria(materia) #se añade la materia que es atributo de un maestro
		
	def setMateria(self, materia):
		self.__materiaQueImparte = materia
	
	def getMateria(self):
		return self.__materiaQueImparte
