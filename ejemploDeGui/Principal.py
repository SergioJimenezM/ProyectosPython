#encoding: utf-8
#!/usr/local/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel('Hola Mundo')
label.show()
app.exec_()
