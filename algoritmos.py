import matplotlib.pyplot as plt

print ("ingrese la cantidad de procesos a realizar")
lista=[]
TP= 0 #Tiempo desarrollo
TT = 0 #Tiempo total
N = int(input("\n >> "))
for i in range (N) :
    NP= input(f"ingrese nombre proceso {i} \n >>")
    DP= int(input(f"ingrese duración proceso {i} \n >>"))
    P= input(f"ingrese prioridad del proceso {i} \n >>")
    
    dic={"Nombre_proceso" : NP,
         "Duracion_proceso " : DP,
         "Prioridad_proceso" : P}
    lista.append(dic)
int(input("ingrese Q \n >>"))
print(lista[0]["Nombre_proceso"]) #INGRESAR AL NOMBRE DEL PROCESO EN LOS DICCIONARIOS
 #tiempo de desarrollo
