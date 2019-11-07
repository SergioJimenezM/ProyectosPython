#!/usr/local/bin/python3
#coding:utf-8

class persona():
	__nombre = ""
	__apellido = ""
	__edad = 0
	
	def __init__(self, nombre, apellido, edad):
		self.setNombre(nombre)
		self.setApellido(apellido)
		self.setEdad(edad)
		
	def setNombre(self, nombre):
		self.__nombre = nombre
	
	def getNombre(self):
		return self.__nombre
	
	def setApellido(self, apellido):
		self.__apellido = apellido
	
	def getApellido(self):
		return self.__apellido
		
	def setEdad(self, edad):
		try:
			edad = int(edad) #intenta convertir el contenido de edad a un tipo numerico
		except:#captura cualquier error
			print("La edad debe ser numerica")
		self.__edad = edad #pasa la edad de el objeto temporal al atributo global __edad
		
	def getEdad(self):
		return self.__edad
