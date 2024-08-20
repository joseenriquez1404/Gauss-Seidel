import numpy as np
import os
#Esto es una calculadora de sistemas de ecuaciones usando el metodo de Gauss Seidel
flag = True

def Gauss_Seidel():
    size = int(input("Ingresa el tamaño del sistema de ecuaciones: "))
    matrizA = np.zeros((size, size), dtype=float)
    matrizB = np.zeros(size, dtype=float)
    valuesX = np.zeros(size, dtype=float)
    PastValues = np.zeros(size, dtype=float)
    Errors = np.full(size, 100, dtype=float)
    iteracion = 0

    #Se procede a pedir los datos al usuario
    for i in range(size):
        for j in range(size):
            matrizA[i, j] = float(input(f"Ingrese el valor para la posicion ({i+1}, {j+1}): "))

    for i in range(size):
        matrizB[i] = float(input(f"Ingresa los terminos independientes del sistema de ecuaciones de la fila {i+1}: "))

    Error_Deseado = float(input("Ingresa el error deseado: "))


    #Verificamos que la diagonal sea diferente a cero
    diagonal = np.diagonal(matrizA)

    #Falta verificar que la diagonal no sea cero y que sea diagonalmente dominante

    """
    for i in range(size):
        if (diagonal[i] == 0.0):
            raise ValueError(f"El elemento de la diagonal {i} es 0. Considera reorganiar las filas")

    """

    while np.any(np.abs(Errors) > Error_Deseado):

        iteracion = iteracion + 1

        for i in range(size):
            PastValues[i] = valuesX[i]

        for i in range(size):
            sum = 0
            for j in range(size):
                if (j != i):
                    sum = sum + matrizA[i, j] * valuesX[j]
            
            valuesX[i] = (matrizB[i] - sum) / diagonal[i]

        for i in range(size):
            Errors[i] = np.abs((valuesX[i] - PastValues[i]) / valuesX[i]) * 100


    for i in range(size):
        print(f"El valor de X{i+1} es: {valuesX[i]}")

def Gaussiana():
    size = int(input("Ingresa el tamaño del sistema de ecuaciones"))
    matrizA = np.zeros((size, size + 1), dtype=float)
    
    for i in range(size):
        for j in range(size + 1):
            matrizA[i , j] = float(input(f"Ingresa el valor de la posicion ({i+1}, {j+1}): "))

    pivote = matrizA[0,0]

    for i in range(size):
        matrizA[i] = matrizA[i] / matrizA[i,i]

        for j in range(size):
            if( i != j):
                matrizA[j] = matrizA[j] - matrizA[i] * matrizA[j,i]

    print(matrizA)



def menu():
    print("1. Calculadora mediante Gauss Seidel")
    print("2. Calculadora mediante montante")


while flag:
    os.system('cls')

    menu()
    opcion = int(input("Ingresa la opción deseada: "))
    if opcion == 1:
        Gauss_Seidel()
    if opcion == 2:
        Gaussiana()


    resp = input("¿Quieres ingresar otro sistema de ecuaciones? (S/N): ")
    if(resp == "N" or resp == "n"):
        flag = False

    


        



            
            


    
