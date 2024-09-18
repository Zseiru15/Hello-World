# import time
# def ejercicio1 ():
#     palabra=str(input("por favor ingresar palabra: "))
#     cantidad=int(input("ingrese la cantidad de veces: "))
#     for i in range(cantidad):
#         print ("valor de la variable i:", i+1)
#         time.sleep(2)
#         print(palabra)
#     return palabra
# ejercicio1 ()

# print("------------------------------------------------")

# import time
# def ejercicio2 ():
#     cantidad=int(input("ingrese los años: "))
#     for i in range(cantidad):
#         print ("los años son:", i+1)
#         time.sleep(2)
#         print(i+1)
#     return cantidad
# ejercicio2 ()

# print("------------------------------------------------")

import time
def ejercicio4 ():
    cantidad1=int(input("ingrese su año de nacimiento: "))
    cantidad2=int(input("ingrese el presente año: "))
    cantidad3=cantidad2-cantidad1
    print("la edad es: ", cantidad3)
    for i in range(cantidad3+1):
        print ("los años son:", cantidad1+i)
        time.sleep(2)
        print(i)
    return
ejercicio4 ()

# print("------------------------------------------------")

