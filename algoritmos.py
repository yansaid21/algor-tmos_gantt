#import matplotlib.pyplot as plt

print ("ingrese la cantidad de procesos a realizar")
lista=[]
TE= 0 #Tiempo espera de cada proceso
TR = 0 #Tiempo respuesta de cada proceso
lista_prioridad = []

while True:
    try:
        N = int(input("\n >> "))
        break
    except ValueError:
        print("     !!! VALOR INVÁLIDO, INGRESE UN NÚMERO !!! ")
        
for i in range (N) :
  NP= input(f"ingrese nombre proceso {i} \n >> ")
  while True:
    try:
      DP= int(input(f"ingrese duración proceso {i} \n >> "))
      break
    except ValueError:
      print("     !!! VALOR INVÁLIDO, INGRESE UN NÚMERO !!! ")
  P = input(f"ingrese prioridad del proceso {i} \n >> ")
  dic = {"Nombre_proceso" : NP,
       "Duracion_proceso" : DP,
       "Prioridad_proceso" : P}
  lista_prioridad.append(P)
  lista.append(dic)

while True:
    try:
      int(input("ingrese Q \n >> "))
      break
    except ValueError:
      print("     !!! VALOR INVÁLIDO, INGRESE UN NÚMERO !!! ")

print(lista)
print(lista[0]["Nombre_proceso"]) #INGRESAR AL NOMBRE DEL PROCESO EN LOS DICCIONARIOS
 #tiempo total
suma =0
total = 0
for i in range (N):
  suma += lista[i]["Duracion_proceso"]
  total += suma
TR = total/N
print("TIEMPO DE RESPUESTA")
print(TR)
#TE tiempo de desarrollo
suma = 0
total = 0
for i in range (N-1):
  suma += lista[i]["Duracion_proceso"]
  total += suma
TE = total/N
print("TIEMPO DE ESPERA")
print(TE)
