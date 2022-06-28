# input

from pickle import FALSE

# Input
b= int(input("Número a buscar: "))## Se recibe el número

# Processing

a= [1,2,3,4,5] ## Se hace una lista de datos
r= False ##Se hace una variable con valor falso

for i in a:
    if i==b:
        print("Lo encontre!",b)
        r= True
if r==False:
    print("No lo encontre :/")
    
# Output

print("\nEso era...")
