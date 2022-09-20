import matplotlib.pyplot as plt
import numpy as np

print ("ingrese la cantidad de procesos a realizar")
lista=[]
TE= 0 #Tiempo espera de cada proceso
TR = 0 #Tiempo respuesta de cada proceso
lista_prioridad = []

while True:
    try:
        N = int(input("\n >> ")) #numero de procesos
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

#TIEMPOS
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

#primer diagrama de gant
altura_barras = 10
tticks = 10
procesos = []
rango_horizontal = 0
for i in range (N):
  procesos.append(lista[i]["Nombre_proceso"]) #obtener solo el nombre de los procesos
  rango_horizontal += lista[i]["Duracion_proceso"] #obtener la duración de cada proceso y sumarlo para encontrar hasta donde se extienden las x
      
print(procesos)

# Creación de los objetos del plot:
fig, gantt = plt.subplots()

# Etiquetas de los ejes:
gantt.set_xlabel("Duración")
gantt.set_ylabel("Procesos")

# Límites de los ejes:
gantt.set_xlim(0, rango_horizontal)
gantt.set_ylim(0, N*altura_barras)

# Divisiones de eje x
gantt.grid(True, axis="x")

# Divisiones del eje y
gantt.set_yticks(range(altura_barras, N*altura_barras, altura_barras), minor=True)
gantt.grid(True, axis='y', which='minor')

# Etiquetas de máquinas:
gantt.set_yticks(np.arange(altura_barras/2, altura_barras*N - altura_barras/2 + altura_barras, altura_barras))
gantt.set_yticklabels(procesos)

# "g" = green -> color verde para todos los procesos del algoritmo 1
# t0 = donde inicia el proceso
def agregar_tarea(t0, duracion, proceso, nombre):
  # Índice de la máquina:
  index_proceso = procesos.index(proceso)
  print("procesooo")
  print(procesos[index_proceso])
  # Posición de la barra:
  gantt.broken_barh([(t0, duracion)], (altura_barras*index_proceso, altura_barras), facecolors=("g"))
  # Posición del texto:
  gantt.text(x=(t0 + duracion/2), y=(altura_barras*index_proceso + altura_barras/2), s=f"{nombre} ({duracion})", va='center', color='white')

agregar_tarea(0, lista[0]["Duracion_proceso"],lista[0]["Nombre_proceso"],lista[0]["Nombre_proceso"])
suma = 0
indice = 1
for indice in range (N):
  suma += lista[i]["Duracion_proceso"]
  agregar_tarea(suma, lista[indice]["Duracion_proceso"], lista[indice]["Nombre_proceso"],lista[indice]["Nombre_proceso"])
  print(lista[indice]["Nombre_proceso"])
plt.show()