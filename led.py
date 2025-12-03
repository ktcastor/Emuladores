"""
Script que emula el comportamiento de un led
"""

# Clase que crea un led
class EMULed:
    # Constructor de la clase
    def __init__(self, id=0, on=True, color="green"):
        # Establecemos las propiedades de encendido y color del led
        self.id = id
        self.on = on
        self.color = color

    # Función para ejecutar el emulador
    def play(self):
        # Verificamos que el led se encuentre encendido
        if self.on:
            print(f"Led {self.id} encendido en color {self.color}")
        else:
            print(f"El led {self.id} se encuentra apagado")

    # Funciones para cambiar, encender y apagar el led
    def switch(self):
        self.on = not self.on

    def on_led(self):
        self.on = True

    def off_led(self):
        self.on = False
