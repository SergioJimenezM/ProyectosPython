import os
import sqlite3
from persona import Persona
from dispositivo import Dispositivo

class controlDeDatos:

    def __init__(self):
        self.nombreDB = 'BaseDeDatos.db'
        self.esquemaDB = 'estructuraDeDatos.sql'
        db = not os.path.exists(self.nombreDB)
        conn = sqlite3.connect(self.nombreDB)
        conn.execute("pragma foreign_keys = on")
        if db:
            print("creando tablas")
            with open(self.esquemaDB, 'rt') as archivo:
                esquema = archivo.read()
                print(esquema)
            conn.executescript(esquema)
        conn.close()
    # cambiar el nombreDB implica
    # 1-cambiar el nombre de la db
    # 2-seleccionar un archivo db en otro sitio
    # 3-crear una db nueva y sus tablas
    # 4-quitar la db antigua que puede ser leida desde vscode

    #el archivo esquemaDB contiene todo el esquema de las bases de datos
    #para aplicar el esquema automaticamente hace falta borrar la DB antigua
    #no hay que hacerlo a menos que sea nececesario y siempre luego de recuperar datos

    def conexion(self):
        conn = sqlite3.connect(self.nombreDB)
        return conn

    def listarPersonas(self):
        con = self.conexion()
        consulta = "select * from persona"
        cursor = con.cursor()
        cursor.execute(consulta)
        lista = []
        for nombre, telefono in cursor.fetchall():
            laPersona = Persona(nombre, telefono)
            lista.append(laPersona)
        con.close()
        return lista

    def listarDispositivos(self, laPersona):
        con = self.conexion()
        consulta = "select * from dispositivo where telefono = ?"
        cursor = con.cursor()
        cursor.execute(consulta, (laPersona.getTelefono(),))
        tupla = cursor.fetchall()
        lista = []
        for telefono, descripcion, fechaDeIngreso, fechaDeEntrega, vencimientoDeGarantia in tupla:
            elDispositivo = Dispositivo(telefono, descripcion, fechaDeIngreso, fechaDeEntrega, vencimientoDeGarantia)
            lista.append(elDispositivo)
        con.close()
        return lista

    def agregarPersona(self, laPersona):
        con = self.conexion()
        consulta = "insert into persona(nombre, telefono) values(?,?);"
        cursor = con.cursor()
        cursor.execute(consulta, (laPersona.getNombre(), laPersona.getTelefono(),))
        afectadas = cursor.rowcount
        con.commit()
        con.close()
        return afectadas

    def agregarDispositivo(self, dispositivo):
        con = self.conexion()
        consulta = "insert into dispositivo(telefono, descripcion, fechaDeIngreso, fechaDeEntrega, vencimientoDeGarantia) values(?,?,?,?,?)"
        cursor = con.cursor()
        cursor.execute(consulta, (dispositivo.getTelefono(), dispositivo.getDescripcion(), dispositivo.getFechaDeIngreso(), dispositivo.getFechaDeEntrega(), dispositivo.getVencimientoDeGarantia(),))
        afectadas = cursor.rowcount
        con.commit()
        con.close()
        return afectadas

    def buscarPersona(self, telefono = "", nombre = ""):
        con = self.conexion()
        lista = []
        if telefono:
            consulta = "select * from persona where telefono = ?"
            print("busca por telefono")
            pass
        if nombre:
            consulta = "select * from persona where nombre like ?"
            cursor = con.cursor()
            nombre ='%'+nombre+'%'
            cursor.execute(consulta, (nombre,))
            for nombre, telefono in cursor.fetchall():
                laPersona = Persona(nombre, telefono)
                lista.append(laPersona)
        con.close()
        return lista

    def buscarDispositivo(self):
        pass

    def modificarPersona(self, laPersona):
        pass

    def modificarDispositivo(self, elDispositivo):
        pass


if __name__ == '__main__':
    control = controlDeDatos()
    
    p1 = Persona("Andrey", "1")
    p2 = Persona("Sergio","2")
    
    #print("columnas afectadas", control.agregarPersona(p1))
    #print("columnas afectadas", control.agregarPersona(p2))

    #d1 = Dispositivo(telefono="1",descripcion= "aifron negro pantalla quebrada", fechaDeIngreso="2023/06/21", fechaDeEntrega="2023/07/21", vencimientoDeGarantia="2023/10/21")
    #print("columnas afectadas", control.agregarDispositivo(d1))
    #p1.setDispositivos(d1)

    for i in control.listarPersonas():
        print("Nombre:", i.nombre, "Telefono:", i.telefono)

    for i in control.listarDispositivos(p1):
        print("Telefono:", i.getTelefono(), "Descripcion", i.getDescripcion())

    for i in control.buscarPersona(nombre = "ser"):
        print("Nombre:", i.nombre, "Telefono:", i.telefono)
    