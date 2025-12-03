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
