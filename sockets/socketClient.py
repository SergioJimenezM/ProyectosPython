#!usr/bin/python3
import socket


def cliente():
	servidorIP = socket.gethostname()  #recupera la ip de localhost o se define una ip
	puerto = 1212  #Numero de puerto, se recomienda usar por encima de 1024 por estandar
	
	socketDelCliente = socket.socket()  #se instancia el socket del cliente
	socketDelCliente.connect((servidorIP, puerto))  #se intenta conectar con el servidor
	print("Para cerrar la conexion escriba salir")
	mensajeDelCliente = input("> ")  #recibe texto
	
	while mensajeDelCliente.lower().strip() != "salir":
		socketDelCliente.send(mensajeDelCliente.encode())  #envía por el socket el mensaje codificado
		datosEntrantes = socketDelCliente.recv(1024).decode()  #se recibe y decodifica la respuesta
		print("Servidor responde: " + datosEntrantes)  #se muestra el mensaje
		mensajeDelCliente = input("> ")  #esto debería ser un metodo por tener que repetirse
		
	socketDelCliente.close()  #se cierra la conexion, el canal debe quedar cerrado
	
if __name__ == '__main__':
	cliente()
