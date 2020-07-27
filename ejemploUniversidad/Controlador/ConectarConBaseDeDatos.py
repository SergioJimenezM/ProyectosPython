#!usr/bin/python3

import pymysql as mariadb

usuario = "persona"#esto no se hace
contrasegna = "persona"#esto mucho menos
direccion = "localhost"
baseDeDatos = "Universidad"
puerto = 3306

class ConectarConBaseDeDatos():
	laConexionInstanciada = None
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
		
	def obtenerCursor(self):
		if self.laConexionInstanciada != None:
			cerrarConexion()
			self.laConexionInstanciada = self.conectar()
			
		else:
			self.laConexionInstanciada = self.conectar()
			
		return self.laConexionInstanciada
	
	def confirmarSentencia(self):
		self.laConexionInstanciada.commit()
		self.cerrarConexion()
		
	def revertirSentencia(self):
		self.laConexionInstanciada.rollback()
		self.cerrarConexion()
	
	def cerrarConexion(self):
		self.laConexionInstanciada.close()
		self.laConexionInstanciada = None
		
		
	

if __name__== '__main__':
	print("No se espera que este codigo sea ejecutado sin su contexto")
