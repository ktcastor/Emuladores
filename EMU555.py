# Este es un emulador del circuito integrado NE555

import time
import threading

# Clase que ejecuta el emulador
class EMU555:
    def __init__(self, on=True, time=0.1, keyToExit="q"):
        self.on = on
        self.time = time
        self.keyToExit = keyToExit
        self.fn = None

    # Evento que se ejecuta al completar el tiempo
    def do(self, fn):
        self.fn = fn

    # Función para iniciar el emulador (ticks en bucle)
    def play(self):
        while self.on:
            if self.fn:
                self.fn()
            time.sleep(self.time)


# Testeo del emulador
emu555 = EMU555()

# Función que ejecutará al completar el tiempo establecido
def exect():
    print("Tick")

emu555.do(fn=exect)

# Ejecutamos el emulador en un hilo separado
hilo = threading.Thread(target=emu555.play)
hilo.start()

# Función para esperar la salida
def esperar_salida():
    print(f"Escribe '{emu555.keyToExit}' y presiona Enter para apagar el circuito.")
    while True:
        key = input()
        if key == emu555.keyToExit:
            emu555.on = False
            print("Emulador EMU555 apagado")
            break
        else:
            print("Tecla incorrecta, intenta de nuevo.")

    hilo.join()

# Llamamos a la función de salida
esperar_salida()
