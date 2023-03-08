def separar(a_separar, separador):
    arreglo = list()
    registro = ""
    for letra in a_separar:
        if letra == separador or letra == '\n':
            arreglo.append(registro)
            registro = ""
            continue
        registro += letra
    if letra != "\n":
        arreglo.append(registro)
    return arreglo
def mostrar(arreglo):
    for registro in arreglo:
        print(registro)
def ordena(arr, registro):
    n = len(arr)
    # Recorre todos los elementos del arreglo
    for i in range(n):
        # La última i elementos ya están en su lugar correcto
        for j in range(i+1, n):
            # Compara elementos adyacentes
            if int(arr[j][registro]) < int(arr[i][registro]):
                # Intercambia los elementos si el anterior es mayor que el siguiente
                arr[i], arr[j] = arr[j], arr[i]
debug = True
def deb(texto):
    global debug
    if debug:
        print(texto)
archivo = open("procesos.txt", "r")
separacion = archivo.readlines()
procesos = list()
for registro in separacion:
    procesos.append(separar(registro,","))
print("Procesos de entrada")
mostrar(procesos)
SEPARADOR = "----------------------------------------------"
print(SEPARADOR)