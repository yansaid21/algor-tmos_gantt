import matplotlib.pyplot as plt
import numpy as np
SoloRoundRobinList=[]
Tiempos_Iniciales=[]

print ("ingrese la cantidad de procesos a realizar")
lista=[]
TE= 0 #Tiempo espera de cada proceso
TR = 0 #Tiempo respuesta de cada proceso
lista_prioridad = []
lista_duracion = []
lista_proceso=[]

while True:
    try:
        N = int(input("\n >> ")) #numero de procesos
        break
    except ValueError:
        print("     !!! VALOR INVÁLIDO, INGRESE UN NÚMERO !!! ")

for i in range (1 , N+1) :
  NP= input(f"ingrese nombre proceso {i} \n >> ")
  lista_proceso.append(NP)
  while True:
    try:
      DP= int(input(f"ingrese duración proceso {i} \n >> "))
      break
    except ValueError:
      print("     !!! VALOR INVÁLIDO, INGRESE UN NÚMERO !!! ")
      
  while True:
    try:
      P = int(input(f"ingrese prioridad del proceso {i} \n >> "))
      while(P<1 or P>N):   
        print("INGRESE UN VALOR DENTRO DEL RANGO \n>> ")
        P= int(input(f"ingrese prioridad del proceso {i} \n >> "))
      break
    except ValueError:
      print("     !!! VALOR INVÁLIDO, INGRESE UN NÚMERO !!! ")
      
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
      lista_aux=lista.copy()
      for i in range (N):
            lista_aux.pop(lista_prioridad[i]-1)
            lista_aux.insert(lista_prioridad[i]-1,lista[i])
      return (lista_aux)
            
#función round robin
def round_robin():
  lista_cociente=[]
  lista_aux=[]
  Residuo=[]
  for x in range (N):
    lista_aux.append(lista[x])
  lista_vacia=[]
  lista_respuesta=lista_aux[:]
  acum=[]
  for i in range (N):
    acum.append(int(lista_aux[i]["Duracion_proceso"]/Q))
    
    #acum.append(int(lista_aux[i]["Duracion_proceso"]/Q))
    lista_cociente.append(lista_aux[i]["Duracion_proceso"]/Q)
  for y in range(N):
        lista_respuesta[y]["Duracion_proceso"] = Q
  for i in range (len(acum)):
    Residuo.append(lista_cociente[i]-acum[i])
    if (Residuo[i] != 0) :
      acum[i]+=1   
  for i in range (len(acum)):
    k=i  
    for j in range(acum[i]):
      lista_vacia.insert(k,lista_respuesta[i])
      if (j == acum[i]-1 and Residuo[i] != 0) :
        if(k<len(lista_vacia)):
          lista_vacia.pop(k)
        else:
          lista_vacia.pop()
        duracion_Residuo= (int(Q*lista_cociente[i])-(Q*(acum[i]-1)))
        dic_auxiliar={
          "Nombre_proceso": lista_respuesta[i]["Nombre_proceso"],
          "Duracion_proceso" : duracion_Residuo,
       "Prioridad_proceso" : lista_respuesta[i]["Prioridad_proceso"]
        }
        lista_vacia.insert(k,dic_auxiliar)
      k += i+1
   
  return (lista_vacia)
            
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
  
  for i in range (len(lista)):
    procesos.append(lista[i]["Nombre_proceso"]) #obtener solo el nombre de los procesos
    rango_horizontal += lista[i]["Duracion_proceso"] #obtener la duración de cada proceso y sumarlo para encontrar hasta donde se extienden las x

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
  gantt.set_ylim(0, len(lista)*altura_barras)

  # Divisiones de eje x
  gantt.grid(True, axis="x")

  # Divisiones del eje y
  gantt.set_yticks(range(altura_barras, len(lista)*altura_barras, altura_barras), minor=True)
  gantt.grid(True, axis='y', which='minor')

  # Etiquetas de máquinas:
  gantt.set_yticks(np.arange(altura_barras/2, altura_barras*(len(lista)) - altura_barras/2 + altura_barras, altura_barras))
  gantt.set_yticklabels(procesos)
  return diagrama_dict
''' 
"g" = green -> color verde para todos los procesos del algoritmo 1
t0 = donde inicia el proceso 
d = duración de cada proceso, es decir, hasta donde va el proceso
map = proceso = nombre del proceso 
 '''

def agregar_tarea(diagrama, t0, duracion, proceso, nombre,indice):
  lista_numeros=[]
  #recuperar variables del diagrama 
  procesos = diagrama["procesos"]
  altura_barras = diagrama["altura_barras"]
  gantt = diagrama["ax"]
  # Índice de la máquina:
  #index_proceso = procesos.index(proceso)
  for i in range(len(procesos)):
    lista_numeros.append(i)    
  # Posición de la barra:
  gantt.broken_barh([(t0, duracion)], (altura_barras*lista_numeros[indice], altura_barras), facecolors=("g"))
  # Posición del texto:
  gantt.text(x=(t0 + duracion/2), y=(altura_barras*lista_numeros[indice] + altura_barras/2), s=f"{nombre} ({duracion})", va='center', color='white')

def mostrar_diagrama(lista, nombre_diagrama):
  diagrama = crear_diagrama_vacio(lista, nombre_diagrama)
  '''Todos los procesos comienzan en 0, por tal motivo primero se agrega el primer proceso de la lista en t0 = 0'''
  agregar_tarea(diagrama, 0, lista[0]["Duracion_proceso"],lista[0]["Nombre_proceso"],lista[0]["Nombre_proceso"],0)
  suma = 0
  for i in range (1, len(lista)): #es decir que arranca desde la posicion 1 y va hasta N
    suma += lista[i-1]["Duracion_proceso"]
    agregar_tarea(diagrama, suma, lista[i]["Duracion_proceso"], lista[i]["Nombre_proceso"],lista[i]["Nombre_proceso"],i)

  plt.show()

def mostrar_diagramaRobin(lista, nombre_diagrama):
  suma_doble_aux=0
  suma_aux=0
  SoloRoundRobinDic={}
  diagrama = crear_diagrama_vacio(lista, nombre_diagrama)
  '''Todos los procesos comienzan en 0, por tal motivo primero se agrega el primer proceso de la lista en t0 = 0'''
  agregar_tarea(diagrama, 0, lista[0]["Duracion_proceso"],lista[0]["Nombre_proceso"],lista[0]["Nombre_proceso"],0)
  suma = 0
  SoloRoundRobinDic={"nombre" : (diagrama["procesos"][0]),
                     "tiempo_final": lista[0]["Duracion_proceso"]}
  InicialesRoundRobinDic={"nombre" : (diagrama["procesos"][0]),
                     "tiempo_inicial": 0}
  Tiempos_Iniciales.append(InicialesRoundRobinDic)
  SoloRoundRobinList.append(SoloRoundRobinDic)
  suma_aux= lista[0]["Duracion_proceso"]
  for i in range (1, len(lista)): #es decir que arranca desde la posicion 1 y va hasta N
    suma += lista[i-1]["Duracion_proceso"]
    suma_doble_aux += lista[i]["Duracion_proceso"]
    suma_aux += lista[i]["Duracion_proceso"]
    InicialesRoundRobinDic={"nombre" : (diagrama["procesos"][i]),
                        "tiempo_inicial":(suma_doble_aux)}
    Tiempos_Iniciales.append(InicialesRoundRobinDic)
    SoloRoundRobinDic={"nombre" : (diagrama["procesos"][i]),
                        "tiempo_final":(suma_aux)}
    SoloRoundRobinList.append(SoloRoundRobinDic)
    ''' print("dictionary")
    print(SoloRoundRobinList) '''
    agregar_tarea(diagrama, suma, lista[i]["Duracion_proceso"], lista[i]["Nombre_proceso"],lista[i]["Nombre_proceso"],i)

  plt.show()
def tiempoRespuestaRogbinhood():
  banderita=False
  sumatoria=0
  inverseRobinList=SoloRoundRobinList.copy()
  inverseRobinList.reverse()
  for j in range (N):
    banderita=False
    i=0
    while(banderita==False):
      if(lista_proceso[j]==inverseRobinList[i]["nombre"]):
            sumatoria+=inverseRobinList[i]["tiempo_final"]
            banderita=True
      i+=1
  total=sumatoria/N
  print ("TIEMPO RESPUESTA")
  print(total)
      
def TiempoEsperaRoundRobin():
  bandera=False
  total=0
  suma=0
  for i in range (N):
    bandera=False
    j=i
    for x in range (len(SoloRoundRobinList)):
      if(SoloRoundRobinList[j]["nombre"] == lista_proceso[i] and Tiempos_Iniciales[x]["nombre"] == lista_proceso[i] and bandera==True):
        aux=Tiempos_Iniciales[x]["tiempo_inicial"]-SoloRoundRobinList[j]["tiempo_final"]
        if(aux>=0):    
          suma+=aux
          j=x
      elif(SoloRoundRobinList[j]["nombre"] == lista_proceso[i] and Tiempos_Iniciales[x]["nombre"] == lista_proceso[i] and bandera==False):
        suma += Tiempos_Iniciales[x]["tiempo_inicial"]
        bandera=True
  total=suma/N
  print("TIEMPO DE ESPERA")
  print(total)    

print("-----------------------------------------TIEMPOS DE ALGORITMO FCFS (ORDEN DE LLEGADA)-----------------------------------------")
mostrar_diagrama(lista, "FCFS (ORDEN DE LLEGADA)")
tiempo_espera(lista)
tiempo_respuesta(lista)

print("-----------------------------------------TIEMPOS DE ALGORITMO SJF (PRIMERO EL MÁS CORTO)--------------------------------------")
algoritmo2 = primero_mas_corto(lista_duracion)
mostrar_diagrama(algoritmo2, "SJF (PRIMERO EL MÁS CORTO)")
tiempo_espera(algoritmo2)
tiempo_respuesta(algoritmo2)

#prioridades
print("-----------------------------------------TIEMPOS DE ALGORITMO PLANIFICACIÓN BASADA EN PRIORIDADES-----------------------------")
algoritmo3=prioridades_metod(lista_prioridad)
mostrar_diagrama(algoritmo3, "Planificación basada en prioridades")
tiempo_espera(algoritmo3)
tiempo_respuesta(algoritmo3)

print("-----------------------------------------TIEMPOS DE ALGORITMO ROUND ROBIN(TURNO ROTATIVO)-------------------------------------")
algoritmo4=round_robin()
mostrar_diagramaRobin(algoritmo4,"Round-Robin")
tiempoRespuestaRogbinhood()
TiempoEsperaRoundRobin()
