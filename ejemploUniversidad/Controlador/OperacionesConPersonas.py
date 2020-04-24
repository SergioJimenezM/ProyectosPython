#!/usr/bin/python3
import sys
from datetime import date
sys.path.append("../")
#La unica forma de importar es subir un directorio, pero me parece feo
from Modelo.Persona import Persona
from Controlador.ConectarConBaseDeDatos import ConectarConBaseDeDatos

class OperacionesConPersonas():
	
	def insertarPersona(self, persona):
		instancia = ConectarConBaseDeDatos()
		conexion = instancia.conectar()
		cursor = conexion.cursor()
		filas = 0
		sql = "insert into Personas values (%s, %s, %s, %s, %s, %s)" 
		try:
			filas = cursor.execute(sql, (persona.getDNI, persona.getPrimerNombre, persona.getSegundoNombre, persona.getPrimerApellido, persona.getSegundoApellido, persona.getFechaDeNacimiento,))
			conexion.commit()
			conexion.close()
		except Exception as e:
			conexion.rollback()
			conexion.close()
			return "Ha ocurrido un error ", e.args#Los errores nunca deben pasar silenciosamente
		print(filas)
		return filas
	
	def buscarPersonaPorDNI(self, dni):
		instancia = ConectarConBaseDeDatos()
		conexion = instancia.conectar()
		cursor = conexion.cursor()
		sql = "select * from Personas where DNI = %s;"
		try:
			cursor.execute(sql, (dni,))
			conexion.close()
		except Exception as e:
			conexion.close()
			return "Ha ocurrido un error ", e.args
		registro = cursor.fetchone()#Sacar uno
		laPersona = Persona(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
		print(laPersona)
		print(laPersona.getPrimerNombre())
		return laPersona
		
	def listarPersonas(self):#Se lista por nombres o apellidos
		instancia = ConectarConBaseDeDatos()
		conexion = instancia.conectar()
		cursor = conexion.cursor()
		sql = "SELECT * FROM Personas;"
		try:
			cursor.execute(sql)
			conexion.close()
		except Exception as e:
			conexion.close()
			return "Ha ocurrido un error ", e.args
		listaDePersonas = []
		for registro in cursor.fetchall():
			listaDePersonas.append(Persona(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]))
		return listaDePersonas
		
	def eliminarPersona(self, persona):
		instancia = ConectarConBaseDeDatos()
		conexion = instancia.conectar()
		cursor = conexion.cursor()
		sql = "delete from Personas where DNI = %s"
		try:
			cursor.execute(sql, persona.getDNI)
			conexion.commit()
			conexion.close()
		except Exception as e:
			conexion.rollback()
			conexion.close()
			return "Ha ocurrido un error ", e.args
		
	
	def actualizarPersona(self, persona):
		
		pass
		
if __name__=='__main__':
	conexion = OperacionesConPersonas()
	listaDePersonas = conexion.listarPersonas()
	
