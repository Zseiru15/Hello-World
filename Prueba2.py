def suma_dos_valores(a, b):
    global resultado
    resultado = a + b
    return resultado

# suma_dos_valores(4, 5)
# print("primera suma")
# print(resultado)
# suma_dos_valores(1,2)
# print("segunda suma")
# print(resultado)

# def calculadora_dos_valores(a, b, operador):
#     global resultado
#     if operador==1: #si el operador es 1 es una suma
#         resultado = a + b
#         return resultado
#     elif operador==2: #si el operador es 2 es una resta
#         resultado = a - b
#         return resultado
#     elif operador==3: #si el operador es 3 es una multiplicacion
#         resultado = a * b
#         return resultado
#     elif operador==4: #si el operador es 4 es una division
#         resultado = a / b
#         return resultado
#     else: #si el operador es otro numero
#         print("el numero ingresado no es valido")
#     return resultado

# print("------------------------------------------------")

# calculadora_dos_valores(1,2,1)
# print("suma: ",resultado)
# calculadora_dos_valores(1,2,2)
# print("resta: ",resultado)
# calculadora_dos_valores(1,2,3)
# print("multiplicacion: ",resultado)
# calculadora_dos_valores(1,2,4)
# print("division: ",resultado)

# print("------------------------------------------------")

# def pitagoras(a,b):
#     global c
#     c=(a**2+b**2)**0.5
#     return c
# pitagoras(3,4)
# print("pitagoras: ",c)

# print("------------------------------------------------") 

# def despeje_x():
#     global x
#     b=int(input("ingrese el valor de b: "))
#     c=int(input("ingrese el valor de c: "))
#     x=(c-b)/2
#     print("el valor de x es: ",x)
#     return x
# despeje_x()

# print("------------------------------------------------") 

# def compuerta():
#     global x
#     a=bool(input("ingrese el valor de a: "))
#     print(a)
#     b=bool(input("ingrese el valor de b: "))
#     print(b)
#     c=bool(input("ingrese el valor de c: "))
#     print(c)
#     x= a and b and c
#     print("el valor de x es: ",x)
#     return x
# compuerta()

# print("------------------------------------------------") 

# def pitagoras_funcion_sumar():  
#     global resul_pitagoras
#     a=int(input("ingrese el valor de a: "))
#     b=int(input("ingrese el valor de b: "))
#     a2= a**2
#     b2= b**2
#     suma= suma_dos_valores(a2,b2)
#     resul_pitagoras=suma**0.5
#     print("el valor de pitagoras es: ",resul_pitagoras)
#     return resul_pitagoras
# pitagoras_funcion_sumar()



# def letras():
#     global conteo
#     palabra=input("ingrese la palabra: ")
#     letra=input("ingrese la letra: ")
#     conteo=palabra.count(letra)
#     print("la letra ",letra," aparece ",conteo," veces en la palabra")
#     return conteo
# letras()

# print("------------------------------------------------")

# def cantidad_letras():
#     global conteo, conteo2
#     palabra=str(input("ingrese la palabra: "))
#     conteo=len(palabra)
#     conteo2=list(palabra)
#     print("la palabra tiene ",conteo," letras")
#     print("las letras son: ",conteo2,)
#     return conteo
# cantidad_letras()

# print("------------------------------------------------")

# def eleccion():
#     import random
#     usuario1= random.choice(["piedra", "papel", "tijera"])
#     print(usuario1)
#     usuario2=random.choice(["piedra", "papel", "tijera"])
#     print(usuario2)
#     if usuario1==usuario2:
#         print("empate")
#     elif (usuario1 == "piedra" and usuario2 == "tijera"):
#         print("usuario1 gana")
#     elif (usuario1 == "tijera" and usuario2 == "papel"):
#         print("usuario1 gana")
#     elif (usuario1 == "papel" and usuario2 == "piedra"):
#         print("usuario1 gana")
#     else:
#         print("usuario2 gana")
#     return   
# eleccion()

# print("------------------------------------------------")