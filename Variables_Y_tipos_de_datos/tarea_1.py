"""
    El limite de los enteros en python es de 9223372036854775807
    el limite de los flotantes es de 1.7976931348623157e+308
"""

string = "Hola Soy Luis A"
entero = 28
flotante = 100.0

resultado = string+" tengo"+" "+str(entero)+" años y espero obtener una nota de "+str(flotante)+ " en esta ruta"
print(resultado)

#Aplicar la formula de la suma de los primeros n numeros pares, tomando con n la variable entera
#  y almacenar el resultado en la variable

#Pido por teclado al usuario
num_float = float(input("Ingrese numero n: "))
#Aplicar formula
result = (num_float*(num_float+1))/2
#Imprimir el resultado
print(f'El resultados es: {result}')