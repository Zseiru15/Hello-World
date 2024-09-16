import time
print("Hello") #Esta linea imprime en consola la palabra hola
print("Hello World \n")
time.sleep(3)
print("Segundo renglon") 

print(type("Hello")) #La funcion type me dice que tipo de dato es lo que esta en los parentesis
print(type(4))
print(type(5.5))
print("pruebagitignore")

print("------------------------------------------------")
bool=True
print(bool)
print(type(bool))
numero=5
texto="hola"
suma=str(numero)+texto
print(suma)
bool1=True
bool2=False
suma2=bool1+bool2
print(suma2)

A=False
B=False
C=False
D=True
S=((A and B) and C) or D
print("El resultado es: ",S)

A2=True
B2=True
C2=True
D2=True
S2=((A and B) and C) or D
print("El resultado es: ",S2)

S3=(A and B and C and D)
print("El resultado es: ",S3)