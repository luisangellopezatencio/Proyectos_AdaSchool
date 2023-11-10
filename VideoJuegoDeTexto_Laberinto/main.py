from readchar import readkey, key

#Pedir el nombre del jugador
name = input("Ingrese su nombre: ")
#Imprimir el nombre
print("Hola", name)

#Iniciar el juego
trigger = True
while trigger:
    print("Presione una tecla para continuar")
    tecla = readkey()
    print(f'Haz presionado la tecla {tecla}')
    if tecla == key.UP:
        print("Saliendo del juego")
        trigger = False