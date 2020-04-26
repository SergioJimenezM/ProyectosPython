#!usr/bin/python3
import sys
from datetime import date
sys.path.append("../")
#La unica forma de importar es subir un directorio, pero me parece feo
from Modelo.Persona import Persona
from Controlador.ConectarConBaseDeDatos import ConectarConBaseDeDatos

class OperacionesConPersonas():
	
	def insertarPersona(self, laPersona):
		instancia = ConectarConBaseDeDatos()
		conexion = instancia.conectar()
		cursor = conexion.cursor()
		filas = 0
		sql = "insert into Personas values (%s, %s, %s, %s, %s, %s)" 
		try:
			filas = cursor.execute(sql, (laPersona.getDNI(), laPersona.getPrimerNombre(), laPersona.getSegundoNombre(), laPersona.getPrimerApellido(), laPersona.getSegundoApellido(), laPersona.getFechaDeNacimiento(),))
			conexion.commit()
			conexion.close()
		except Exception as e:
			conexion.rollback()
			conexion.close()
			return "Ha ocurrido un error "+e.args#Los errores nunca deben pasar silenciosamente
		if filas == 0:
			return "No se han insertado registros"
		else:
			return "Se ha insertado "+str(filas)+" registro(s)"
	
	def buscarPersonaPorDNI(self, dni):
		instancia = ConectarConBaseDeDatos()
		conexion = instancia.conectar()
		cursor = conexion.cursor()
		filas = 0
		sql = "select * from Personas where DNI = %s;"
		try:
			filas = cursor.execute(sql, (dni,))#esto evita que realice inyección de codigo sql
			conexion.close()
		except Exception as e:
			conexion.close()
			return "Ha ocurrido un error "+e.args
		if(filas == 0):
			return "No hay registros"
		registro = cursor.fetchone()#Sacar uno
		laPersona = Persona(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
		return laPersona
		
	def listarPersonas(self):#Se lista por nombres o apellidos
		instancia = ConectarConBaseDeDatos()
		conexion = instancia.conectar()
		cursor = conexion.cursor()
		filas = 0
		sql = "SELECT * FROM Personas;"
		try:
			filas = cursor.execute(sql)
			conexion.close()
		except Exception as e:
			conexion.close()
			return "Ha ocurrido un error "+e.args
			
		if filas == 0:
			return "No hay registros"
		listaDePersonas = []
		for registro in cursor.fetchall():
			listaDePersonas.append(Persona(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]))
		return listaDePersonas
		
	def eliminarPersona(self, laPersona):
		instancia = ConectarConBaseDeDatos()
		conexion = instancia.conectar()
		cursor = conexion.cursor()
		filas = 0
		sql = "delete from Personas where DNI = %s"
		try:
			filas = cursor.execute(sql, laPersona.getDNI())
			conexion.commit()
			conexion.close()
		except Exception as e:
			conexion.rollback()
			conexion.close()
			return "Ha ocurrido un error "+e.args
		if filas == 0:
			return "No se ha podido eliminar"
		else:
			return "Se han borrado "+str(filas)+" registro(s)"
	
	def actualizarPersona(self, laPersona):
		instancia = ConectarConBaseDeDatos()
		conexion = instancia.conectar()
		cursor = conexion.cursor()
		filas = 0
		sql = "update Personas set PrimerNombre = %s, SegundoNombre = %s, PrimerApellido = %s, SegundoApellido = %s, FechaDeNacimiento = %s where DNI = %s"
		try:
			filas = cursor.execute(sql, (laPersona.getPrimerNombre(), laPersona.getSegundoNombre(), laPersona.getPrimerApellido(), laPersona.getSegundoApellido(), laPersona.getFechaDeNacimiento(), str(laPersona.getDNI())))
			conexion.commit()
			conexion.close()
		except Exception as e:
			conexion.rollback()
			conexion.close()
			return "Ha ocurrido un error "+e.args
		if filas == 0:
			return "No se ha podido actualizar"
		else:
			return "Se ha actualizado "+str(filas)+" registro(s)"
		
if __name__=='__main__':
	print("No se espera que este codigo sea ejecutado sin su contexto")
