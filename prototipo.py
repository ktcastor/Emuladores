"""

Script para propar los emuladores creados en python

"""

#importamos los emuladores y las librerias necesarias
import threading

#Emulador del led
from led import EMULed

#Emulador del circuito integrado CD4017
from EMUCD4017 import EMUCD4017

#EMulador del circuito integrado NE555
from EMU555 import EMU555


#Creamos una instancia del emulador EMUCD4017
emucd4017 = EMUCD4017()

#Obtenmos el pin actual activo del emulador 
p, v = list(emucd4017.getPin().items())[0]

#Creamos 10 leds que interactuarán con los pines del circuito
leds = [EMULed(id = _) for _ in range(10)]

#Encendemos el primer led
if v == True:
	print(f"El pin {p} del emulalador EMUCD4017 esta activo")
	leds[p].play()

"""
Creamos una instancia del emualador EMU555
con sus valores por defecto:

	Encendido
	1.0 = 1 segundo
	q = tecla q para terminar el bucle

"""
emu555 = EMU555(time = 1.0)

#Creamos una funcion que se va a ejecutar cuando el tiempo establecido en el EMU555 se complete
def ex():

	global p,v

	#Apagamos el led activo y encendemos el siguiente 
	leds[p].off_led()

	emucd4017.switchPin() 

	#Obtenmos el pin actual activo del emulador 
	p, v = list(emucd4017.getPin().items())[0]

	#Encendemos el siguente led o regresamos al primero
	if v == True:
		leds[p].on_led()
		print(f"El pin {p} del emulalador EMUCD4017 esta activo")
		leds[p].play()

#Agregamos la funcion a ejecutar al emulador EMU555
emu555.do(fn = ex)

"""
Activamos el tick del emulador EMU555 para iniciar la emulacion del prototipo en un hilo separado, que no trabe la aplicación
Ejecutamos el emulador en un hilo separado
"""
hilo = threading.Thread(target=emu555.play)
hilo.start()

#Función que dentendra el EMU555  y terminar la ejecución del prototipo
def salida():
    print(f"Escribe '{emu555.keyToExit}' y presiona Enter para apagar el circuito.")
    while True:
        key = input()
        if key == emu555.keyToExit:
            emu555.on = False
            print("Ejecución del prototipo finalizada")
            break
        else:
            print("Tecla incorrecta, intenta de nuevo.")

    hilo.join()

# Llamamos a la función de salida
salida()