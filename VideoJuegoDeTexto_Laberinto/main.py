from readchar import readkey, key
import os
import random

#Pedir el nombre del jugador
name = input("Ingrese su nombre: ")
#Imprimir el nombre
print("Hola", name)

class Game:
    def __init__(self, laberinto, initialPoint, name):
        self.laberinto = laberinto
        self.initialPoint = initialPoint
        self.name = name
        self.trigger = True

    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')  #Borrar la consola


    def string_to_caracters_matrix(self, string: str):
        """
            Esta funcion convierte un string en una matriz de caracteres
        """
        return [list(line) for line in string.split("\n")]

    def clearAndShowMatrix(self, matrix):
        """
            Esta funcion limpia la consola y muestra la matriz
        """
        self.clear()
        for line in matrix:
            print("".join(line))

    def goDown(self,currentPoint):
        currentPoint[0] = currentPoint[0] + 1
        return currentPoint

    def goUP(self, currentPoint):
        currentPoint[0] = currentPoint[0] - 1
        return currentPoint

    def goLEFT(self, currentPoint):
        currentPoint[1] = currentPoint[1] - 1
        return currentPoint

    def goRIGHT(self, currentPoint):
        currentPoint[1] = currentPoint[1] + 1
        return currentPoint

    def mainLoop(self, map, initialPoint, finalPoint):
        trigger = self.trigger
        currentPoint = list(initialPoint)
        while trigger:
            map[currentPoint[0]][currentPoint[1]] = "P"
            self.clearAndShowMatrix(map)
            previousPoint = currentPoint
            map[previousPoint[0]][previousPoint[1]] = "."
            print(currentPoint, finalPoint)
            key_ = readkey()
            if key_ == key.UP:
                if (map[currentPoint[0] - 1][currentPoint[1]] != "#"): #Verificamos que no haya una pared
                    currentPoint = self.goUP(currentPoint)
            elif key_ == key.DOWN:
                if map[currentPoint[0] + 1][currentPoint[1]] != "#":
                    currentPoint = self.goDown(currentPoint)
            elif key_ == key.LEFT:
                if map[currentPoint[0]][currentPoint[1] - 1] != "#":
                    currentPoint = self.goLEFT(currentPoint)
            elif key_ == key.RIGHT:
                if map[currentPoint[0]][currentPoint[1] + 1] != "#":
                    currentPoint = self.goRIGHT(currentPoint)
            else:
                trigger = False
            if tuple(currentPoint) == finalPoint:
                trigger = False
                print(f"{self.name}, Ganaste!")
            
    def start(self):
        map = self.string_to_caracters_matrix(self.laberinto)
        #Punto Final
        Pf = (len(map) - 1, len(map[0])-2)
        self.mainLoop(map, self.initialPoint, Pf)

class GameArchivo():
    def __init__(self, name):
        self.name = name
    def leer_archivos_txt(self):
        path_carpeta = "laberintos"
        archivos = os.listdir(path_carpeta)
        archivo = random.choice(archivos)
        

        mapa = """"""
        with open(f"{path_carpeta}/{archivo}") as archivo:
            mapa += archivo.read()

        return mapa
    def init(self):
        laberinto = self.leer_archivos_txt()
        P0 = (0,0)
        self.game = Game(laberinto, P0, self.name)
        #ejecutamos el juego
        self.game.start()

        
        
        

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""


P0 = (0,0)

#instanciamos la clase
#game = Game(laberinto, P0, name)

#ejecutamos el juego
#game.start()

gameArchivo = GameArchivo(name)
gameArchivo.init()

#Hacer archivos para clases