#!/usr/local/bin/python3
#coding:utf-8

#del archivo X importamos la clase X como etiqueta X
from Persona import persona as Persona
from Maestro import maestro as Maestro

def menu():
	opcion = input("1 - Crear una persona \n2 - Crear un maestro\n3 - salir\n")
	if(opcion == '1'):
		crearPersona()
		
	elif(opcion == '2'):
		crearMaestro()
		
	else: 
		exit()	

def crearPersona():
	laPersona = Persona(input("ingrese el nombre\n"), input("ingrese el apellido\n"), input("ingrese la edad\n"))
	laPersona.mostrarDatos()
	
def crearMaestro():
	elMaestro = Maestro(input("ingrese el nombre\n"), input("ingrese el apellido\n"), input("ingrese la edad\n"), input("ingrese la materia\n"))
	elMaestro.mostrarDatos()

if(__name__ == '__main__'):
    while(True):
        menu()
