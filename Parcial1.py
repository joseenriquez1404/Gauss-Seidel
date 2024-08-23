import numpy as np
import os
#Esto es una calculadora de sistemas de ecuaciones usando el metodo de Gauss Seidel
flag = True


def Gaussiana():
    size = int(input("Ingresa el tamaño del sistema de ecuaciones: "))
    matrizA = np.zeros((size, size + 1), dtype=float)

    for i in range(size):
        for j in range(size + 1):
            matrizA[i][j] = int(input(f"Ingresa el elemento de la posicion ({i+1}, {j+1}): "))

    for k in range(size):
        for i in range(k+1, size):
            factor = matrizA[i][k] / matrizA[k][k]
            for j in range(k, size+1):
                matrizA[i][j] = matrizA[i][j] - (factor * matrizA[k][j])

    terminos_independientes = matrizA[:, -1]

    for i in range(size - 1, -1, -1):
        suma = 0
        for j in range(i + 1, size):
            suma += matrizA[i][j] * terminos_independientes[j]
        terminos_independientes[i] = (matrizA[i][-1] - suma) / matrizA[i][i]

    print(terminos_independientes)





def Gauss_Seidel():
    size = int(input("Ingresa el tamaño del sistema de ecuaciones: "))
    matrizA = np.zeros((size, size), dtype=np.float64)
    matrizB = np.zeros(size, dtype=np.float64)
    valuesX = np.zeros(size, dtype=np.float64)
    PastValues = np.zeros(size, dtype=np.float64)
    Errors = np.full(size, 100, dtype=np.float64)
    iteracion = 0
    dominante = True

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



    for i in range(size):
        sum = 0
        for j in range(size):
            if(i != j):
                sum = sum + matrizA[i][j]

        if (diagonal[i] < sum):
            dominante = False

    if dominante == True:
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
            print(f"El valor de X{i + 1} es: {valuesX[i]}")
    else:
        print("El sistema no es dominante. Intenta reordenar el sistema y vuelve a ingresarlo")




def Gauss_Jordan():
    size = int(input("Ingresa el tamaño del sistema de ecuaciones"))
    matrizA = np.zeros((size, size + 1), dtype=float)
    
    for i in range(size):
        for j in range(size + 1):
            matrizA[i , j] = float(input(f"Ingresa el valor de la posicion ({i+1}, {j+1}): "))


    for i in range(size):
        matrizA[i] = matrizA[i] / matrizA[i,i]

        for j in range(size):
            if( i != j):
                matrizA[j] = matrizA[j] - matrizA[i] * matrizA[j,i]

    print(matrizA)



def menu():
    print("1. Calculadora mediante Gauss Seidel")
    print("2. Calculadora mediante Gauss - Jordan")
    print("3, Calculadora mediante el metodo Gaussiano")


while flag:
    os.system('cls')

    menu()
    opcion = int(input("Ingresa la opción deseada: "))
    if opcion == 1:
        Gauss_Seidel()
    elif opcion == 2:
        Gauss_Jordan()
    elif opcion == 3:
        Gaussiana()


    resp = input("¿Quieres ingresar otro sistema de ecuaciones? (S/N): ")
    if(resp == "N" or resp == "n"):
        flag = False


    


        



            
            


    
