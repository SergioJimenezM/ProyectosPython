#encoding: utf-8
#!/usr/local/bin/python3
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

#favor borrar mucha mierda cuando no sean las 11 de la noche
#las pulsaciones de teclado se leen con el script en segundo plano
#una lectura del teclado sin interrupciones requiere una gran responsabilidad

startStop = KeyCode(char='-')#se dispara en true cuando se presiona la tecla
salida = KeyCode(char=',')#lease comentario anterior
keyCambiaDelay = KeyCode(char='.')#este ya es por vicio, pero igual que el otro

posicion1 = {0,0}
posicion2 = {0,0}
delay = 90

print("Instrucciones\n presione - para iniciar repeticion\n \
	presione . para cambiar el delay general\n \
	presione , para cerrar el programa")
	
class ClickMouse(threading.thread):
	def __init__(self, delay):
		super(ClickMouse, self).__init__()
		self.delay = delay
		self.running = False
		self.program_running = True
		self.posicion1 = posicion1
		self.posicion2 = posicion2
	
	def cambiaDelay(self, delay):
		self.delay = delay
	
	def stop_clicking(self):
		print("*clicking music stop*")
		self.running = False
	
	def start_clicking(self):
		print("*clicking intensifies*")
		self.running = True
	
	def exit(self):
		print("*clicking band has been killed*")
		self.stop_clicking()
		self.program_running = False
		
	def run(self):
		while self.program_running:
			
			while self.running:
				mouse.position = 1399, 227
				time.sleep(1)
				mouse.click(Button.right)
				time.sleep(1)
				mouse.position = 1449, 278
				time.sleep(0.5)
				mouse.click(Button.left)
				time.sleep(self.delay)
			time.sleep(0.1)
                        
mouse = Controller()
click_thread = ClickMouse(delay)
click_thread.start()


def on_press(key):
    if key == startStop:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == salida:
        click_thread.exit()
        listener.stop()
        exit()
    elif key == keyCambiaDelay:
        global delay
        print("Ingrese delay nuevo: ", delay)
        delay = int(input())
        click_thread.cambiaDelay(delay)

with Listener(on_press=on_press) as listener:
    listener.join()

