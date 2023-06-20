class Persona:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.dispositivos = []
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getTelefono(self):
        return self.telefono 
    
    def setTelefono(self, telefono):
        self.telefono = telefono

    def getDispositivos(self):
        return self.dispositivos
    
    def setDispositivos(self, listaDispositivos):
        self.dispositivos = listaDispositivos
