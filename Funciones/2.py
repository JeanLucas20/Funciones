
def buscarDatosEnLista(datoABuscar , lista):
    r= False
    for i in lista:
        if i== datoABuscar:
            r= True
    return r

# Input
dato= int(input("Número a buscar: ")) #Se recibe el dato del usuario

# Processimg
lista= [1,2,3,4,5]
if buscarDatosEnLista(dato, lista):
    print("Lo encontre!!!")
else:
    print("No lo encontre :/")

print("\nEso era...")
