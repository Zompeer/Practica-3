from main import *

print("SJF")
tiempo = 0
ordenEjecucion = list()
ordena(procesos, 1)
print(SEPARADOR)
print("Procesos ordenados")
mostrar(procesos)

while(True):
    if not procesos:
        break
    print(SEPARADOR)
    print("Tiempo: "+str(tiempo))
    print(SEPARADOR)
    tiempo+=1
    if int(procesos[0][1]) == 0:
        print("Ejecucion Finalizada "+str(procesos[0]))
        ordenEjecucion.append(procesos[0])
        procesos.pop(0)
        if procesos:
            print("Ejecutando "+str(procesos[0]))
            procesos[0][1] = str(int(procesos[0][1])-1)
    else:
        print("Ejecutando "+str(procesos[0]))
        procesos[0][1] = str(int(procesos[0][1])-1)
print("\nOrden de finalizacion")
mostrar(ordenEjecucion)
input()