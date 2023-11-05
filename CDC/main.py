import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPlainTextEdit, QLineEdit, QPushButton, QDateEdit
from datetime import date
from dateutil.relativedelta import relativedelta

#pip install Pyside6
#pip install python-dateutil

from controlDeDatos import controlDeDatos
from dispositivo import Dispositivo
from persona import Persona

raiz = None
con = controlDeDatos()
laPersona = None

class ventanaPrincipal(QDialog):
    def __init__(self, parent = None):
        super(ventanaPrincipal, self).__init__(parent)
        raiz.setWindowTitle("Andrews Industries Catalog")
        self.instancia()
        pass

    def instancia(self):
        #Layout general
        layoutGeneral = QVBoxLayout()

        #Layout horizontal
        layoutHorizontal = QHBoxLayout()

        #Layout central
        layoutIzquierda = QVBoxLayout()
        
        self.lblNombre = QLabel("Nombre de cliente")
        layoutIzquierda.addWidget(self.lblNombre)

        self.txtNombre = QLineEdit()
        layoutIzquierda.addWidget(self.txtNombre)
        
        self.lblTelefono = QLabel("Telefono de cliente")
        layoutIzquierda.addWidget(self.lblTelefono)

        self.txtTelefono = QLineEdit()
        layoutIzquierda.addWidget(self.txtTelefono)

        self.lblDescripcion = QLabel("Descripcion del dispositivo")
        layoutIzquierda.addWidget(self.lblDescripcion)

        self.txtDescripcion = QLineEdit()
        layoutIzquierda.addWidget(self.txtDescripcion)

        self.lblFechaDeIngreso = QLabel("Fecha de ingreso")
        layoutIzquierda.addWidget(self.lblFechaDeIngreso)
        hoy = date.today()
        self.dateFechaDeIngreso = QDateEdit()
        self.dateFechaDeIngreso.setDisplayFormat("dd-MM-yyyy")
        self.dateFechaDeIngreso.setCalendarPopup(True)
        self.dateFechaDeIngreso.setDate(hoy)
        layoutIzquierda.addWidget(self.dateFechaDeIngreso)

        self.lblFechaDeEntrega = QLabel("Fecha de entrega")
        layoutIzquierda.addWidget(self.lblFechaDeEntrega)

        self.dateFechaDeEntrega = QDateEdit()
        self.dateFechaDeEntrega.setDisplayFormat("dd-MM-yyyy")
        self.dateFechaDeEntrega.setCalendarPopup(True)
        self.dateFechaDeEntrega.setDate(hoy)
        layoutIzquierda.addWidget(self.dateFechaDeEntrega)

        self.lblVencimientoDeGarantia = QLabel("Vencimiento de garantía")
        layoutIzquierda.addWidget(self.lblVencimientoDeGarantia)

        hoy = hoy + relativedelta(months=3)
        
        self.dateVencimientoDeGarantia = QDateEdit()
        self.dateVencimientoDeGarantia.setDisplayFormat("dd-MM-yyyy")
        self.dateVencimientoDeGarantia.setCalendarPopup(True)
        self.dateVencimientoDeGarantia.setDate(hoy)
        layoutIzquierda.addWidget(self.dateVencimientoDeGarantia)

        #Layout derecha
        layoutDerecha = QVBoxLayout()

        self.btnAgregarPersona = QPushButton("Agregar Persona")
        self.btnAgregarPersona.clicked.connect(self.agregarPersona)
        layoutDerecha.addWidget(self.btnAgregarPersona)

        self.btnBuscarPersona = QPushButton("Buscar Persona")
        self.btnBuscarPersona.clicked.connect(self.buscarPersona)
        layoutDerecha.addWidget(self.btnBuscarPersona)

        self.btnListarPersonas = QPushButton("Listar personas")
        self.btnListarPersonas.clicked.connect(self.listarPersonas)
        layoutDerecha.addWidget(self.btnListarPersonas)

        self.btnLimpiar = QPushButton("Limpiar")
        self.btnLimpiar.clicked.connect(self.limpiar)
        layoutDerecha.addWidget(self.btnLimpiar)

        #layout inferior
        layoutInferior = QVBoxLayout()
        self.mostrarError = QPlainTextEdit()
        self.mostrarError.setReadOnly(True)
        layoutInferior.addWidget(self.mostrarError)

        #Ordenar los layout
        layoutHorizontal.addLayout(layoutIzquierda)
        layoutHorizontal.addLayout(layoutDerecha)
        layoutGeneral.addLayout(layoutHorizontal)
        layoutGeneral.addLayout(layoutInferior)
        self.setLayout(layoutGeneral)

        #Redimensionar ventana a los elementos
        self.adjustSize()

    def agregarPersona(self):
        print("esto no debería tocarse solo")
        laPersona = Persona(self.txtNombre.text(), self.txtTelefono.text())
        string = con.agregarPersona(laPersona)
        self.limpiar()
    
    def buscarPersona(self):
        telefono = self.txtNombre.text()
        nombre = self.txtTelefono.text()

        if(not nombre and not telefono):
            self.mostrarError.setPlainText("Debe ingresar un nombre o telefono")
        elif(not nombre):
            self.mostrarError.setPlainText("Nombre")
        elif(not telefono):
            self.mostrarError.setPlainText("Telefono")
        
    def listarPersonas(self):
        pass

    def listarDispositivos(self):
        pass

    def llenarObjeto(self, laPersona):
        pass

    def vaciarObjeto(self):
        
        pass
    
    def limpiar(self):
        self.txtNombre.setText("")
        self.txtTelefono.setText("")
        self.txtDescripcion.setText("")
        self.mostrarError.setPlainText("")

if __name__=='__main__':
    app = QApplication(sys.argv)
    raiz = QMainWindow()
    raiz.setCentralWidget(ventanaPrincipal()).__init__()
    raiz.show()
    sys.exit(app.exec())