"""
Este es un emulador del circuito integrado CD4017 en Python
para poder usarlo en proyectos propios.
"""

# Clase del emulador
class EMUCD4017:

    # Constructor de la clase
    def __init__(self, on=True):
        self.on = on
        self.pins = [False for _ in range(10)]
        self.count = 0           # Q0 activo al inicio
        self.pins[self.count] = True

    # Avanza a la siguiente salida (simula un pulso de reloj)
    def switchPin(self):
        if self.on:
            self.pins[self.count] = False
            self.count = (self.count + 1) % 10
            self.pins[self.count] = True

    # Obtiene el pin actual encendido
    def getPin(self):
        return {self.count: self.pins[self.count]}