from readchar import readkey, key
import os

#Pedir el nombre del jugador
name = input("Ingrese su nombre: ")
#Imprimir el nombre
print("Hola", name)

#Iniciar el juego
trigger = True

def clear():
    os.system('cls' if os.name=='nt' else 'clear')  #Borrar la consola

def increment():
    global count
    count = count + 1

def string_to_caracters_matrix(string: str):
    """
        Esta funcion convierte un string en una matriz de caracteres
    """
    return [list(line) for line in string.split("\n")]

def clearAndShowMatrix(matrix):
    """
        Esta funcion limpia la consola y muestra la matriz
    """
    clear()
    for line in matrix:
        print("".join(line))

def goDown(currentPoint):
    currentPoint[0] = currentPoint[0] + 1
    return currentPoint

def goUP(currentPoint):
    currentPoint[0] = currentPoint[0] - 1
    return currentPoint

def goLEFT(currentPoint):
    currentPoint[1] = currentPoint[1] - 1
    return currentPoint

def goRIGHT(currentPoint):
    currentPoint[1] = currentPoint[1] + 1
    return currentPoint

def mainLoop(map, initialPoint, finalPoint):
    global trigger
    currentPoint = list(initialPoint)
    while trigger:
        map[currentPoint[0]][currentPoint[1]] = "P"
        clearAndShowMatrix(map)
        previousPoint = currentPoint
        map[previousPoint[0]][previousPoint[1]] = "."
        key_ = readkey()
        if key_ == key.UP:
            if (map[currentPoint[0] - 1][currentPoint[1]] != "#"): #Verificamos que no haya una pared
                currentPoint = goUP(currentPoint)
        elif key_ == key.DOWN:
            if map[currentPoint[0] + 1][currentPoint[1]] != "#":
                currentPoint = goDown(currentPoint)
        elif key_ == key.LEFT:
            if map[currentPoint[0]][currentPoint[1] - 1] != "#":
                currentPoint = goLEFT(currentPoint)
        elif key_ == key.RIGHT:
            if map[currentPoint[0]][currentPoint[1] + 1] != "#":
                currentPoint = goRIGHT(currentPoint)
        else:
            trigger = False
        
        

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


matrix_laberinto = string_to_caracters_matrix(laberinto)

#Punto Inicial
P0 = (0,0)
#Punto Final
Pf = (len(matrix_laberinto) - 1, len(matrix_laberinto[0]) - 1)

#Ejecutar el juego
mainLoop(matrix_laberinto, P0, Pf)