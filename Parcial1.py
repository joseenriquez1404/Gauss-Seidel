import numpy as np
import os
#Esto es una calculadora de sistemas de ecuaciones usando el metodo de Gauss Seidel
flag = True

def ingresar_datos(matrizA, size):
    for i in range(size):
        for j in range(size+1):
            matrizA[i][j] = float(input(f"Ingresa el valor de la posición {i+1} , {j+1}: "))

def reordenar_filas(matrizA, size):
    cambio = False
    for fila in range(size):
        if (matrizA[fila][fila] == 0):
            iteracion = 0
            while (cambio == False) and (iteracion < size):
                if (fila != iteracion):
                    if(matrizA[iteracion][fila] != 0):
                        matrizA[[fila, iteracion]] = matrizA[[iteracion, fila]]
                        cambio = True
                iteracion = iteracion + 1
        cambio = False
    print(matrizA)

def reordenar_columnas(matrizA, size):

    for fila in range(size):
        suma = 0
        for columna in range(size):
            if columna != fila:
                suma += np.abs(matrizA[fila][columna])

        if np.abs(matrizA[fila][fila]) < suma:
            # Busca la columna con el mayor valor absoluto fuera de la diagonal
            max_col = -1
            max_val = -1
            for iteracion in range(size-1):
                if iteracion != fila:
                    if np.abs(matrizA[fila][iteracion]) > max_val:
                        max_val = np.abs(matrizA[fila][iteracion])
                        max_col = iteracion

            if max_col != -1:
                # Intercambia columnas para hacer la matriz diagonalmente dominante
                matrizA[:, [fila, max_col]] = matrizA[:, [max_col, fila]]


    print(matrizA)

def Dominante(matrizA, size):
    for fila in range(size):
        suma_fuera_diagonal = 0
        for columna in range(size):
            if columna != fila:
                suma_fuera_diagonal += np.abs(matrizA[fila][columna])
        if np.abs(matrizA[fila][fila]) < suma_fuera_diagonal:
            return False
    return True




def Gaussiana(matrizA, size):

    reordenar_filas(matrizA, size)
    flag = True

    diagonal = np.diagonal(matrizA)

    for fila in range(size):
        if (diagonal[fila] == 0):
            flag = False

    if flag:
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



def Gauss_Seidel(matrizA, size):
    matrizB = np.zeros(size, dtype=float)
    valuesX = np.zeros(size, dtype=float)
    PastValues = np.zeros(size, dtype=float)
    Errors = np.full(size, 100, dtype=float)
    iteracion = 0

    matrizB = matrizA[:, -1]

    Error_Deseado = float(input("Ingresa el error deseado: "))

    # Verificación de dominancia diagonal
    reordenar_columnas(matrizA, size)
    reordenar_filas(matrizA, size)

    dominante = Dominante(matrizA, size)
    if dominante:

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
    else:
        print("El sistema no es diagonalmente dominante")

def Gauss_Jordan(matrizA, size):

    reordenar_filas(matrizA, size)

    for i in range(size):
        # Normalizar la fila actual
        matrizA[i] = matrizA[i] / matrizA[i, i]

        # Eliminar las otras entradas en la columna i
        for j in range(size):
            if i != j:
                matrizA[j] = matrizA[j] - matrizA[i] * matrizA[j, i]

    print("Matriz resultante (identidad a la izquierda y soluciones a la derecha):")
    print(matrizA)

def Montante(matrizA):
    matrizB = np.zeros((size, size + 1), dtype=int)
    pivAnt = 1

    # Aplicar la eliminación de Gauss
    for fila in range(size):
        pivAct = matrizA[fila][fila]

        # Actualizar la matriz fila por fila
        for fila_j in range(size):
            if fila_j != fila:  # No modificar la fila del pivote actual
                for columna in range(size + 1):
                    matrizB[fila_j][columna] = ((matrizA[fila][fila] * matrizA[fila_j][columna]) -
                                                (matrizA[fila_j][fila] * matrizA[fila][columna])) / pivAnt

        # Actualizar el pivote anterior
        pivAnt = pivAct

    terminos_independientes = matrizB[:,-1]

    for fila in range(size):
        for columna in range(size):
            if (fila == columna):
                terminos_independientes[fila] = terminos_independientes[fila] / matrizB[fila][fila]
    # Imprimir la matriz resultante

    print("La matriz B resultante es:")
    print(terminos_independientes)

def menu():
    print("1. Calculadora mediante eliminación gaussiana")
    print("2. Calculadora mediante Gauss - Jordan")
    print("3. Calculadora mediante Gauss-Seidel")
    print("4. Calculadora mediante Montante")


while flag:
    os.system('cls')
    menu()
    opcion = int(input("Ingresa la opción deseada: "))
    size = int(input("Ingresa el tamaño del sistema de ecuaciones: "))
    matrizA = np.zeros((size, size + 1), dtype=float)
    ingresar_datos(matrizA, size)
    if opcion == 1:
        Gaussiana(matrizA, size)
    elif opcion == 2:
        Gauss_Jordan(matrizA, size)
    elif opcion == 3:
        Gauss_Seidel(matrizA, size)
    elif opcion == 4:
        Montante(matrizA)


    resp = input("¿Quieres ingresar otro sistema de ecuaciones? (S/N): ")
    if(resp == "N" or resp == "n"):
        flag = False
    os.system('cls')
