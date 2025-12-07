"""
Esta libreria es para crea una emulación de un cpu propio creado
por mi por su amiga cassie para que lo puedan testear y probar

simulara un procesador de 8 bits como el de la ness o otros dispositivos
que llegaron a usar ese tipo de procesadores

tiene licencia GPLV3 por lo que lo pueden usar en sus simulaciones o 
proyectos
"""


#Creamos la clase del procesador Dayanna
class CPUDayana():

    #Definimos su constructor
    def __init__(self):

        self.space = [0x00] * 256 #256 bytes para la memoria principal

        self.A = 0x00 # A sera nuestro acumulador, un acumulador es donde almacenamos números

        self.counter = 0x00 #Contador que ira desplazandose por el programa  bytes x bytes

        self.memory = [0x00] * 256 # Espacio donde se almacenará el programa y resultados en memoria


    #Definimos una función que cargara un programa en el procesador dayana
    def loadProgram(self,program=[]):

        self.program = program

        #Recorremos cada uno de los bytes del programa y los almacenamos en memoria
        for i, b in enumerate(self.program):
            self.memory[i] = b

    #Ejecutamos el procesador
    def run(self):

        while True:

            #Extraemos las instruciones del programa almacenadas en memoria
            instruction = self.memory[self.counter]

            # Si la instrucción es 0, terminamos el programa
            if instruction == 0x00:
                break

            # Si la instrucción es 16, Sumamos nuevos números al acumulador
            elif instruction == 0x10:
                value = self.memory[self.counter + 1]
                self.A = (self.A + value) & 0xFF  # mantenemos 8 bits
                self.counter += 2

            # Si la instrucción es 138, Guardamos el valor del acumulador en memoria
            elif instruction == 0x8A:
                location = self.memory[self.counter + 1]
                self.memory[location] = self.A
                self.counter += 2

            # Si la instrucción es 161, Asignamos un valor númerico a almacenador
            elif instruction == 0xA1:
                self.A = self.memory[self.counter + 1]
                self.counter += 2

            #Retornamos false si alguna instrucion no es conocida 
            else:
                print(f"Error de instruccion en {instruction}")
                break 

        #Mostramos el resultado
        print(f"Acumulador A: {hex(self.A)}")
        print(f"Memoria {self.memory}")
        print(f"Contador final: {hex(self.counter)}")




if __name__ == "__main__":

    #Creamos una instancia del procesador Dayana
    cpu = CPUDayana()

    # 1.- Creamos un programa el cual le estamos diciendo que al acumulador del procesador tiene que inciarlo con el valor 42
    # 2.- Despues tiene que sumarle 6 y luego volverle a sumar 10
    # 3.- luego almacenar el valor del acumulador en memoria 
    # 4.- terminar el programa
    program = [0xA1,42,0x10,8,0x10,10,0x8A,0x10,0x00]

    #Cargamos el programa en el emulador
    cpu.loadProgram(program)

    #Ejecutamos el programa
    cpu.run()
