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

        self.A = 0x00 # A sera nuestro acumulador, un acumulador es donde almacenamos números

        self.counter = 0x00 #Contador que ira desplazandose por el programa  bytes x bytes

        self.memory = [0x00] * 1024 # Espacio de 1 kb donde se almacenará el programa y resultados en memoria


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

            #Si la instrucción es 32, movemos el contador a una posición anterior o siguente
            #Esto da un efecto de bucle o saltos de instrucciones dependiendo de como la usemos
            elif instruction == 0x20:
                location = self.memory[self.counter + 1]
                self.counter = location

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


"""
Clase para ejecutar el ensamblador del cpu Dayana y 
ejecutar los programas escritos para ella.

"""

#Clase que combierte el código dass que es el ensamblador de dayana a programa que dayanna puede leer
class DASS():

    #definimos su constructor el cual le pasamos como parametro el codigo dass
    def __init__(self,program = ""):

        self.program = program

    #función que compila el codigo dass en programa dayanna
    def compile(self):

        self.dayanaProgram = []
        
        for line in self.program.splitlines():

            print(line)

            if "LOAD" in line:

                instructions = line.split()
                self.dayanaProgram.append(0xA1)
                self.dayanaProgram.append(int(instructions[1]))

            
            elif "ADD" in line:

                instructions = line.split()
                self.dayanaProgram.append(0x10)
                self.dayanaProgram.append(int(instructions[1]))

            elif "JUMP" in line:

                instructions = line.split()
                self.dayanaProgram.append(0x20)
                self.dayanaProgram.append(int(instructions[1]))

            elif "STORE" in line:

                instructions = line.split()
                self.dayanaProgram.append(0x8A)
                self.dayanaProgram.append(int(instructions[1]))

            elif "END" in line:

                instructions = line.split()
                self.dayanaProgram.append(0x00)
                self.dayanaProgram.append(int(instructions[1]))

    #Funcion para correr el programa que dayana puede leer en el procesador
    def run(self):

        #Creamos una instancia del procesador dayana
        dayana  = CPUDayana()

        #Cargamos el programa al CPU
        dayana.loadProgram(program= self.dayanaProgram)

        #ejecutamos el procesador
        dayana.run()








if __name__ == "__main__":


    #Creamos un codigo ensamblador en dass que el compilador de dayana puede leer

    dassCode = """

    LOAD 42
    ADD 8
    JUMP 8
    ADD 10
    ADD 20
    STORE 32
    END 0

    """

    #Creamos una instancia del compilador dass
    dass = DASS(program=dassCode)

    #Compilamos el programa codigo hexadecimal que puede leer dayana
    dass.compile()

    #Ejecutamos el programa
    dass.run()



    #Creamos una instancia del procesador Dayana
    #cpu = CPUDayana()

    # 1.- Creamos un programa el cual le estamos diciendo que al acumulador del procesador tiene que inciarlo con el valor 42
    # 2.- Despues tiene que sumarle 6 y luego volverle a sumar 10
    # 3.- luego almacenar el valor del acumulador en memoria 
    # 4.- terminar el programa
    #program = [
                #Almacenamos en el acumulador el valor númerico 42
    #            0xA1,42,
                
                #Le sumamos al acumulador el número 8
    #            0x10,8,
                
                #Saltamos hasta la poscicion 8 del programa
    #            0x20,8,
                
                #Esta instruccion no se ejecuta porque se pasos en el porgrama
    #            0x10,10,
                
                #Se suma el número 20 al acumulador
    #            0x10,20,

                #Almacenamos el valor del acumulador en la celda  32 de la memoria               
    #            0x8A,0x20,
                
                #Terminamos el programa
    #            0x00
    #            ]

    #Cargamos el programa en el emulador
    #cpu.loadProgram(program)

    #Ejecutamos el programa
    #cpu.run()
