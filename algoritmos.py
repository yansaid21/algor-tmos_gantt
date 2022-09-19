print ("ingrese la cantidad de procesos a realizar")
lista=[]
N = int(input("\n >> "))
for i in range (N) :
    NP= input(f"ingrese nombre proceso {i} \n >>")
    DP= input(f"ingrese duración proceso {i} \n >>")
    P= input(f"ingrese prioridad del proceso {i} \n >>")
    
    dic={"Nombre_proceso" : NP,
         "Duracion_proceso " : DP,
         "Prioridad_proceso" : P}
    lista.append(dic)
int(input("ingrese Q \n >>"))
print(lista)
