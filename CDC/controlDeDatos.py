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
        print("Filas afectadas",cursor.rowcount)
        lista = []
        for nombre, telefono in cursor.fetchall():
            laPersona = Persona(nombre, telefono)
            lista.append(laPersona)
        return lista

    def listarDispositivos(self):
        pass

    def agregarPersona(self, laPersona):
        con = self.conexion()
        consulta = "insert into persona(nombre, telefono) values(?,?);"
        cursor = con.cursor()
        cursor.execute(consulta, (laPersona.nombre, laPersona.telefono,))
        afectadas = cursor.rowcount
        con.commit()
        con.close()
        return afectadas

    def agregarDispositivo(self, dispositivo):
        con = self.conexion()
        consulta = "insert into dispositivo(telefono, descripcion, fechaDeEntrega, VencimientoDeGarantia) values(?,?,?,?)"
        pass

    def buscarPersona(self):
        pass

    def buscarDispositivo(self):
        pass

    def modificarPersona(self):
        pass

    def modificarDispositivo(self):
        pass


if __name__ == '__main__':
    control = controlDeDatos()
    
    p1 = Persona("Andrey", "1")
    p2 = Persona("Sergio","2")
    
    print("columnas afectadas", control.agregarPersona(p1))
    print("columnas afectadas", control.agregarPersona(p2))

    for i in control.listarPersonas():
        print("Nombre:", i.nombre, "Telefono:", i.telefono)