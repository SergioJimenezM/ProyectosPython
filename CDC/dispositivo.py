class Dispositivo:
    def __init__(self, telefono, descripcion, fechaDeIngreso, fechaDeEntrega, vencimientoDeGarantia):
        self.telefono = telefono
        self.descripcion = descripcion
        self.fechaDeIngreso = fechaDeIngreso
        self.fechaDeEntrega = fechaDeEntrega
        self.vencimientoDeGarantia = vencimientoDeGarantia
    
    def getTelefono(self):
        return self.telefono

    def setTelefono(self, telefono):
        self.telefono = telefono
    
    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def getFechaDeIngreso(self):
        return self.fechaDeIngreso
    
    def setFechaDeIngreso(self, fechaDeIngreso):
        self.fechaDeIngreso = fechaDeIngreso
        pass
    
    def getFechaDeEntrega(self):
        return self.fechaDeEntrega
    
    def setFechaDeEntrega(self, fechaDeEntrega):
        self.fechaDeEntrega = fechaDeEntrega
    
    def getVencimientoDeGarantia(self):
        return self.vencimientoDeGarantia
    
    def setVencimientoDeGarantia(self, vencimientoDeGarantia):
        self.vencimientoDeGarantia = vencimientoDeGarantia

if __name__=='__main__':
    pass