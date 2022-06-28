"""Construir una funcion que reciba su nombre como parametro y que lo muestre 5 veces en pantalla """

# Input
name= input("Dime tu nombre: ")
a= 0

# processing
def Nombre(name):
    if a==0:
        print("Hola " + name + "!")
        print("Hola " + name + "!")
        print("Hola " + name + "!")
        print("Hola " + name + "!")
        print("Hola " + name + "!")
#Output
Nombre(name)  

print("-------------------------------------------------------------------------------------------------------")

def RepetirNombre(name):
    for RepetirNombre in range(0, 5):
        print(name)
RepetirNombre(name)
