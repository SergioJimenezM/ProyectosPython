#!/usr/bin/python3

import pymysql as mariadb

usuario = "persona"#esto no se hace
contrasegna = "persona"#esto mucho menos
direccion = "localhost"
baseDeDatos = "Universidad"
puerto = 3306

class ConectarConBaseDeDatos():
	
	def configurarConexion(self, user, pas, host, port):
		usuario = user
		contrasegna = pas
		direccion = host
		puerto = port
	
	def conectar(self):
		try:
			conexion = mariadb.connect(host = direccion, port = puerto, user= usuario, password = contrasegna, db = baseDeDatos)
		except Exception as e:
			print("Ha ocurrido un error\n", e)
		return conexion
		


if __name__== '__main__':
	con = ConectarConBaseDeDatos()
	conexion = con.conectar()
	cursor = conexion.cursor()
	print(cursor)
	cursor.close()#Siempre hay que cerrar las conexiones
