import time
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

# import time
# def ejercicio4 ():
#     cantidad1=int(input("ingrese su año de nacimiento: "))
#     cantidad2=int(input("ingrese el presente año: "))
#     cantidad3=cantidad2-cantidad1
#     print("la edad es: ", cantidad3)
#     for i in range(cantidad3+1):
#         print ("los años son:", cantidad1+i)
#         time.sleep(2)
#         print(i)
#     return
# ejercicio4 ()

# print("------------------------------------------------")

# def numeros_impares():
#     numero = int(input("ingrese el numero: "))
#     for i in range(1, numero+1, 1):
#         time.sleep(1)
#         print(i, end=", ")
#         if i == 15:
#             break;
# numeros_impares()

# print("------------------------------------------------")

# def reloj_seg():
#     tiempo = int(input("ingrese el tiempo: "))
#     for i in range(1, 60+1, 1):
#         time.sleep(1)
#         print("tiempo: ",i)
#         if i == tiempo:
#             break;
#     print ("\33[101m" + "tiempo terminado" + "\33[0m")
# reloj_seg()

# print("------------------------------------------------")

# def reloj_seg2():
#     tiempo = int(input("ingrese el tiempo: "))
#     for i in range(1, 60+1, 1):
#         time.sleep(1)
#         print("tiempo: ",i)
#         if i == tiempo:
#             break;
#     print ("\33[101m" + "tiempo terminado" + "\33[0m")
# reloj_seg2()

# print("------------------------------------------------")

# def interes():
#     cantidad=int(input("ingrese la cantidad: "))
#     interes_anual=int(input("ingrese el interes anual: "))
#     tiempo=int(input("ingrese el tiempo de inversion: "))
#     valor=cantidad
#     for i in range(tiempo):
#         calculo1=(valor*interes_anual)/100
#         calculo2=valor+calculo1
#         valor=calculo2
#         time.sleep(1)
#         print("el año ",i+1," ",valor)
#     print ("\33[4m" + "las ganancias en ",tiempo," años son: ",valor," " + "\33[0m")
# interes()

# print("------------------------------------------------")

# def numeros():
#     cantidad=int(input("ingrese la cantidad de asteriscos: "))
#     for i in range(cantidad+1):
#         print("*" * i)
# numeros()

# print("------------------------------------------------")

# def descubir_contraseña():
#     contraseña="123456789"
#     contraseña_ingresada=""
#     intento_ingresado=int(input("por favor ingrese la cantidad de intentos: "))
#     intento=1
#     while contraseña_ingresada != contraseña :
#         contraseña_ingresada=str(input("ingrese la contraseña: "))
#         if contraseña_ingresada != contraseña:
#             print("contraseña incorrecta")
#         elif contraseña_ingresada==contraseña:
#             print("contraseña correcta")
#             break
#         if intento==intento_ingresado:
#             print("se llego al limite de intentos")
#             break
#         intento=intento+1
# descubir_contraseña()

# def descubir_contraseña():
#     contraseña="123456789"
#     contraseña_ingresada=""
#     intentos=0
#     while contraseña_ingresada != contraseña :
#         contraseña_ingresada=str(input("ingrese la contraseña: "))
#         intentos+=1
#         if intentos==3:
#             print("se han excedido los intentos, el programa se cerrará")
#             break
#         elif contraseña_ingresada!= contraseña:
#             print("Contraseña incorrecta, intento ", intentos)
# descubir_contraseña()

# print("------------------------------------------------")

# def frase():
#     palabra=str(input("por favor ingresar palabra: "))
#     letra=str(input("ingrese la letra: "))
#     contador=0
#     for i in palabra:
#         if i==letra:
#             contador=contador+1
#     print("la letra (",letra,") aparece (",contador,") veces en la palabra")
#     return
# frase()

# def frase():
#     palabra=str(input("por favor ingresar palabra: "))
#     letra=str(input("ingrese la letra: "))
#     for i in letra:
#         conteo=palabra.count(letra)
#         print("la letra (",letra,") aparece (",conteo,") veces en la palabra")
#     return
# frase()

# print("------------------------------------------------")

