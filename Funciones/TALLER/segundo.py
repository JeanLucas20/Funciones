"""Funcion que reciba una cadena digitada (Como parametro por el usuario) y que lo muetre n veces en la pantalla. el valor n tambien es ingresado por la persona."""


# Input
frase= input("Sueltate hay una frase:)\n ")
b= int(input("¿ Cuántas veces quieres que se repita ?\n"))

# processing
def Nombre(frase):
    for i in range (0, b):
        print(frase)
Nombre(frase)  

