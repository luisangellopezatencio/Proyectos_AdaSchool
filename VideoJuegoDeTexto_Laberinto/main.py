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

count = 0
while trigger:
    print("Presione una tecla n para continuar")
    tecla = readkey()
    #print(f'Haz presionado la tecla {tecla}')
    if tecla == key.UP:
        print("Saliendo del juego")
        trigger = False
    elif tecla == "n":
        clear()
        print(count)
        increment()
        if count > 50:
            print("Saliendo del juego")
            trigger = False