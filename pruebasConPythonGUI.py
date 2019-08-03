#!usr/bin/python3
import time
from threading import Thread
import pyautogui
"""
print(pyautogui.size())#resolución de la pantalla de la forma n-1
print(pyautogui.position())#posicion actual del mouse

x,y = pyautogui.position()
x += 50
y -= 10
"""
#pyautogui.moveTo(x,y)
"""
mueve el mouse a la posicion deseada
pasar None como coornenada mantiene la posicion
existen argumentos especiales para decorar el movimiento y hacerlo natural
pyautogui.easeInQuad = inicia lento, termina rápido
easeIoutQuad = inicia rapido, termina lento
easeInOutQuad = inicia y termina rápido, pero va lento en medio
easeInElastic = efecto elástico al final del movimiento
"""

#print("el mouse ha sido movido 3 px de la posicion anterior")

#pyautogui.click(clicks = 1, x = 0. y = 0, button = 'right')
"""
donde clicks es el numero de pulsaciones
las posiciones de x y y se pueden omitir
se define el button como el boton presionado
por defecto hace click izquierdo
hay mas metodos pero los parametros de este permiten hacer todo
"""
input("introduzca esta")
print(pyautogui.locateOnScreen('/home/anubarak/CodigoFuente/ProyectosPython/imgPilotoAutomatico/borrar.png'))
