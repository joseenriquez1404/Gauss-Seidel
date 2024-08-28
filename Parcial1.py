import numpy as np
import os
#Esto es una calculadora de sistemas de ecuaciones usando el metodo de Gauss Seidel
flag = True


def Gaussiana():
    flag = False
    size = int(input("Ingresa el tamaño del sistema de ecuaciones: "))
    matrizA = np.zeros((size, size + 1), dtype=float)

    # Llenar la matriz con los valores ingresados por el usuario
    for i in range(size):
        for j in range(size + 1):
            matrizA[i][j] = float(input(f"Ingresa el elemento de la posición ({i + 1}, {j + 1}): "))

    diagonal = np.diagonal(matrizA)

    # Verificar si hay un 0 en la diagonal principal
    for fila in range(size):
        if diagonal[fila] == 0:
            flag = True
            # Intentar intercambiar filas
            for k in range(fila + 1, size):
                if not np.isclose(matrizA[k, fila], 0):
                    matrizA[[fila, k]] = matrizA[[k, fila]]  # Intercambiar filas
                    diagonal = np.diagonal(matrizA)  # Actualizar la diagonal
                    flag = False
                    break

    if not flag:
        for k in range(size):
            for i in range(k + 1, size):
                if matrizA[k][k] != 0:  # Evitar división por 0
                    factor = matrizA[i][k] / matrizA[k][k]
                    for j in range(k, size + 1):
                        matrizA[i][j] = matrizA[i][j] - (factor * matrizA[k][j])
                else:
                    print(f"División por 0 evitada en la fila {k + 1}")
                    return

        terminos_independientes = matrizA[:, -1]

        for i in range(size - 1, -1, -1):
            suma = 0
            for j in range(i + 1, size):
                suma += matrizA[i][j] * terminos_independientes[j]
            if not np.isclose(matrizA[i][i], 0):  # Evitar división por 0
                terminos_independientes[i] = (matrizA[i][-1] - suma) / matrizA[i][i]
            else:
                print(f"División por 0 evitada en la fila {i + 1}")
                return

        print("Soluciones:")
        for i in range(len(terminos_independientes)):
            print(f"X{i+1} = {terminos_independientes[i]}")
    else:
        print("No se pudo evitar un 0 en la diagonal. Modifica el sistema para que no haya un 0 en la diagonal")



def Gauss_Seidel():
    size = int(input("Ingresa el tamaño del sistema de ecuaciones: "))
    matrizA = np.zeros((size, size+1), dtype=float)
    matrizB = np.zeros(size, dtype=float)
    valuesX = np.zeros(size, dtype=float)
    PastValues = np.zeros(size, dtype=float)
    Errors = np.full(size, 100, dtype=float)
    iteracion = 0

    # Solicitud de datos
    for i in range(size):
        for j in range(size+1):
            matrizA[i, j] = float(input(f"Ingrese el valor para la posición ({i + 1}, {j + 1}): "))

    matrizB = matrizA[:, -1]

    Error_Deseado = float(input("Ingresa el error deseado: "))

    # Verificación de dominancia diagonal
    def es_dominante(matriz):
        diagonal = np.diagonal(matriz)
        for i in range(size):
            for j in range(size - 1):
                suma = np.sum(np.abs(matrizA[i][j])) - np.abs(diagonal[i])
                if np.abs(diagonal[i]) < suma:
                    return False
        return True

    # Reordenamiento de la matriz
    def reordenar_matriz(matriz, matrizB):
        indices = np.arange(size)
        for i in range(size):
            for j in range(i + 1, size):
                if np.abs(matriz[indices[j], i]) > np.abs(matriz[indices[i], i]):
                    indices[i], indices[j] = indices[j], indices[i]
                    return matriz[indices], matrizB[indices]

    # Intento de reordenamiento si no es dominante
    if not es_dominante(matrizA):
        matrizA, matrizB = reordenar_matriz(matrizA, matrizB)
        if not es_dominante(matrizA):
            print("No fue posible reordenar el sistema para que sea diagonalmente dominante.")
            return

    diagonal = np.diagonal(matrizA)

    while np.any(np.abs(Errors) > Error_Deseado):

        iteracion += 1
        PastValues[:] = valuesX

        for i in range(size):
            suma = 0
            for j in range(size):
                if j != i:
                    suma += matrizA[i, j] * valuesX[j]

            if diagonal[i] != 0:  # Verificar que no se divida por 0
                valuesX[i] = (matrizB[i] - suma) / diagonal[i]
            else:
                print(f"División por 0 evitada en la fila {i + 1}")
                return  # O manejar de otra manera

        for i in range(size):
            if valuesX[i] != 0:  # Evitar división por 0 al calcular el error
                Errors[i] = np.abs((valuesX[i] - PastValues[i]) / valuesX[i]) * 100
            else:
                Errors[i] = np.inf  # Manejar el error adecuadamente

    for i in range(size):
        print(f"El valor de X{i + 1} es: {valuesX[i]}")

def Gauss_Jordan():
    size = int(input("Ingresa el tamaño del sistema de ecuaciones: "))
    matrizA = np.zeros((size, size + 1), dtype=float)

    for i in range(size):
        for j in range(size + 1):
            matrizA[i, j] = float(input(f"Ingresa el valor de la posición ({i + 1}, {j + 1}): "))

    for i in range(size):
        # Verificar si el pivote es 0
        if matrizA[i, i] == 0:
            # Buscar una fila para intercambiar
            for k in range(i + 1, size):
                if matrizA[k, i] != 0:
                    # Intercambiar filas
                    matrizA[[i, k]] = matrizA[[k, i]]
                    break
            else:
                raise ValueError(
                    f"No se puede continuar porque el pivote en la posición {i + 1} es 0 y no se encontró una fila para intercambiar.")

        # Normalizar la fila actual
        matrizA[i] = matrizA[i] / matrizA[i, i]

        # Eliminar las otras entradas en la columna i
        for j in range(size):
            if i != j:
                matrizA[j] = matrizA[j] - matrizA[i] * matrizA[j, i]

    print("Matriz resultante (identidad a la izquierda y soluciones a la derecha):")
    print(matrizA)

def menu():
    print("1. Calculadora mediante eliminación gaussiana")
    print("2. Calculadora mediante Gauss - Jordan")
    print("3. Calculadora mediante Gauss-Seidel")


while flag:
    os.system('cls')
    menu()
    opcion = int(input("Ingresa la opción deseada: "))
    if opcion == 1:
        Gaussiana()
    elif opcion == 2:
        Gauss_Jordan()
    elif opcion == 3:
        Gauss_Seidel()


    resp = input("¿Quieres ingresar otro sistema de ecuaciones? (S/N): ")
    if(resp == "N" or resp == "n"):
        flag = False
