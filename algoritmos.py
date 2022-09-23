import matplotlib.pyplot as plt
import numpy as np

print ("ingrese la cantidad de procesos a realizar")
lista=[]
TE= 0 #Tiempo espera de cada proceso
TR = 0 #Tiempo respuesta de cada proceso
lista_prioridad = []
lista_duracion = []

while True:
    try:
        N = int(input("\n >> ")) #numero de procesos
        break
    except ValueError:
        print("     !!! VALOR INVÁLIDO, INGRESE UN NÚMERO !!! ")

for i in range (1 , N+1) :
  NP= input(f"ingrese nombre proceso {i} \n >> ")
  while True:
    try:
      DP= int(input(f"ingrese duración proceso {i} \n >> "))
      break
    except ValueError:
      print("     !!! VALOR INVÁLIDO, INGRESE UN NÚMERO !!! ")
  P = int(input(f"ingrese prioridad del proceso {i} \n >> "))
  
  dic = {"Nombre_proceso" : NP,
       "Duracion_proceso" : DP,
       "Prioridad_proceso" : P}
  lista_duracion.append(DP)
  lista_prioridad.append(P)
  lista.append(dic)
  


while True:
    try:
      Q = int(input("ingrese Q \n >> "))
      break
    except ValueError:
      print("     !!! VALOR INVÁLIDO, INGRESE UN NÚMERO !!! ")


      
################print(lista)
#print(lista[0]["Nombre_proceso"]) #INGRESAR AL NOMBRE DEL PROCESO EN LOS DICCIONARIOS

#primero el más corto
def primero_mas_corto(lista_duracion):
      indice = 0
      nueva_lista=lista.copy()
      max_value = max(lista_duracion)
      for i in range (len(lista_duracion)):
          if lista_duracion[i] < max_value:
                indice = i
                max_value = lista_duracion[i]
      dic_aux = nueva_lista[indice]
      nueva_lista.pop(indice)
      respuesta = []
      respuesta.append(dic_aux)
      
      for i in range(len(nueva_lista)):
            respuesta.append(nueva_lista[i])
      return (respuesta)
    
#función de prioridades
def prioridades_metod(lista_prioridad):
      lista_aux=[]
      for i in range (N):
            lista_aux.insert(lista_prioridad[i]-1,lista[i])
            print (lista_aux)
      return (lista_aux)
            
#función round robin
def round_robin():
  lista_aux=[]
  for x in range (N):
    lista_aux.append(lista[x])
  lista_vacia=[]
  lista_respuesta=lista_aux[:]
  acum=[]
  for i in range (N):
    acum.append(int(lista_aux[i]["Duracion_proceso"]/Q))
    
    #acum.append(int(lista_aux[i]["Duracion_proceso"]/Q))
    print("este entra en acum:")
    print(lista_aux[i]["Duracion_proceso"]/Q)
  for y in range(N):
        lista_respuesta[y]["Duracion_proceso"] = Q
  k = 1
  for i in range (len(acum)):
    for j in range(acum[i]):
      lista_vacia.insert(k,lista_respuesta[i])
      k += i
  print("-------------------------- proceso con q")
  print(lista_vacia)
                  
  #duracion proceso - Q*acum[i]    
            
#TIEMPOS
#TR tiempo desarrollo
def tiempo_respuesta(lista):
  suma = 0
  total = 0
  for i in range (N):
    suma += lista[i]["Duracion_proceso"]
    total += suma
  TR = total/N
  print("TIEMPO DE RESPUESTA")
  print(TR)
#TE tiempo de espera
def tiempo_espera(lista):
  suma = 0
  total = 0
  for i in range (N-1):
    suma += lista[i]["Duracion_proceso"]
    total += suma
  TE = total/N
  print("TIEMPO DE ESPERA")
  print(TE)

#primer diagrama de gant
def crear_diagrama_vacio(lista, nombre_diagrama):
  altura_barras = 10 #hbr
  tticks = 10
  procesos = [] #maquinas
  rango_horizontal = 0 #ht
  
  for i in range (N):
    procesos.append(lista[i]["Nombre_proceso"]) #obtener solo el nombre de los procesos
    rango_horizontal += lista[i]["Duracion_proceso"] #obtener la duración de cada proceso y sumarlo para encontrar hasta donde se extienden las x
  
  print(procesos)

  # Creación de los objetos del plot:
  fig, gantt = plt.subplots()
  
  diagrama_dict = {"fig": fig,
                   "ax": gantt,
                   "altura_barras": altura_barras,
                   "tticks": tticks,
                   "procesos": procesos,
                   "rango_horizontal": rango_horizontal} 

  gantt.set_title(nombre_diagrama)
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
  return diagrama_dict
''' 
"g" = green -> color verde para todos los procesos del algoritmo 1
t0 = donde inicia el proceso 
d = duración de cada proceso, es decir, hasta donde va el proceso
map = proceso = nombre del proceso 
 '''

def agregar_tarea(diagrama, t0, duracion, proceso, nombre):
  #recuperar variables del diagrama 
  procesos = diagrama["procesos"]
  altura_barras = diagrama["altura_barras"]
  gantt = diagrama["ax"]
  # Índice de la máquina:
  index_proceso = procesos.index(proceso)
  # Posición de la barra:
  gantt.broken_barh([(t0, duracion)], (altura_barras*index_proceso, altura_barras), facecolors=("g"))
  # Posición del texto:
  gantt.text(x=(t0 + duracion/2), y=(altura_barras*index_proceso + altura_barras/2), s=f"{nombre} ({duracion})", va='center', color='white')

def mostrar_diagrama(lista, nombre_diagrama):
  diagrama = crear_diagrama_vacio(lista, nombre_diagrama)
  '''Todos los procesos comienzan en 0, por tal motivo primero se agrega el primer proceso de la lista en t0 = 0'''
  agregar_tarea(diagrama, 0, lista[0]["Duracion_proceso"],lista[0]["Nombre_proceso"],lista[0]["Nombre_proceso"])
  suma = 0
  for i in range (1, N): #es decir que arranca desde la posicion 1 y va hasta N
    suma += lista[i-1]["Duracion_proceso"]
    agregar_tarea(diagrama, suma, lista[i]["Duracion_proceso"], lista[i]["Nombre_proceso"],lista[i]["Nombre_proceso"])

  plt.show()

''' 
mostrar_diagrama(lista, "FCFS (ORDEN DE LLEGADA)")
tiempo_espera(lista)
tiempo_respuesta(lista)

algoritmo2 = primero_mas_corto(lista_duracion)
mostrar_diagrama(algoritmo2, "SJF (PRIMERO EL MÁS CORTO)")
tiempo_espera(algoritmo2)
tiempo_respuesta(algoritmo2)

#prioridades
algoritmo3=prioridades_metod(lista_prioridad)
mostrar_diagrama(algoritmo3, "Planificación basada en prioridades")
tiempo_espera(algoritmo3)
tiempo_respuesta(algoritmo3) '''

algoritmo4=round_robin()


