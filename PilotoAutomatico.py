#!usr/bin/python3
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import pyautogui

#una lectura del teclado sin interrupciones requiere una gran responsabilidad
#ojalá no se use con fines malignos, nos conocemos lo suficiente
#y hay gente en 2019 que dice que solo se puede hackear con C o ensamblador
#HA, HA, HA, las risas

keyStartStop = KeyCode(char=',')
keyConfiguration = KeyCode(char='.')
keyExit = KeyCode(char='-')

class ClickMouse(threading.Thread):
	def __init__(self):
		super(ClickMouse, self).__init__()
		self.running = False
		self.program_running = True
		print("se ha iniciado el hilo")
	
	def start_clicking(self):
		self.running = True
	
	def stop_clicking(self):
		self.running = False
	
	def exit(self):
		self.stop_clicking()
		self.program_running = False
	
	def run(self):
		while self.program_running:
			while self.running:
				
				time.sleep(1)
			time.sleep(0.1)

class operaciones():
	def __init__(self, coordinates, action, delay):
		self.coordinates = [0,0]
		self.action = 0
		self.delay = 0


click_thread = ClickMouse()
click_thread.start()

def on_press(key):
	if key == keyStartStop:
		if click_thread.running:
			click_thread.stop_clicking()
		else:
			click_thread.start_clicking()
	elif(key == keyConfiguration):
		#inserteConfiguracionAqui
	elif key == keyExit:
		click_thread.exit()
		listener.stop()

with Listener(on_press=on_press) as listener:
	listener.join()
