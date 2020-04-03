#!usr/bin/python3
import socket


def servidor():
    IpLocal = socket.gethostname() #Se coloca la ip local para escuchar por esa direccion
    Puerto = 1212 #Puerto a la escucha

    socketDelServidor = socket.socket()  #se instancia el socket
    socketDelServidor.bind((IpLocal, Puerto))  #se abre la conexion del socket

    socketDelServidor.listen(2)#espera 2 segundos
    conexion, direccionIp = socketDelServidor.accept()  #se acepta la conexion y direccion del cliente
    print("Se conecta cliente: " + str(direccionIp))
    while True:
        #se recibe un stream de datos no mayor a 1024 bits
        datosEntrantes = conexion.recv(1024).decode()
        if not datosEntrantes:
            #si los datosEntrantes estan en blanco, se salta el ciclo
            break
        print("Se mensaje del cliente: " + str(datosEntrantes))
        datosEntrantes = input(' -> ')
        conexion.send(datosEntrantes.encode())  # send data to the client

    conexion.close()  # close the connection


if __name__ == '__main__':
    servidor()
