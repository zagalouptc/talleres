# Programa para de las tres operaciónes básicas implicadas en la solución de ecuaciones lineales
import pandas as pd
import numpy as np
import numpy as np
import os
os.system('cls')

def MultiplicarFila(M, num_fila, num_fila_multiplo):
    M_nueva = M.copy()
    # Escriba su código aquí: multiplique cada elemento de una fila por un número
    M_nueva[num_fila] =M_nueva[num_fila]*num_fila_multiplo
    return M_nueva

def SumarFilas(M, num_fila_1, num_fila_2, num_fila_1_multiple):
    M_nueva = M.copy()
    # Escriba su código aquí: multiplique una fila por un número y sume la fila con otra
    M_nueva[num_fila_2] =  M_nueva[num_fila_2]+num_fila_1_multiple*M_nueva[num_fila_1]
    return M_nueva

def IntercambiarFilas(M, fila_num_1, fila_num_2):
    M_nueva =M.copy()
    # Escriba su código aquí: Intercambie fila_num_1 y fila_num_2 de la matriz M_nueva
    M_nueva[[fila_num_1, fila_num_2]] = M_nueva[[fila_num_2, fila_num_1]]
    return M_nueva

A_test = np.array([
        [1, -2, 3, -4],
        [-5, 6, -7, 8],
        [-4, 3, -2, 1],
        [8, -7, 6, -5]
    ], dtype=np.dtype(float))

print("Matriz original:")
print(A_test)

print("\nMatriz original después de multiplicar su tercera fila por -2:")
print(MultiplicarFila(A_test, 2, -2))

print("\nMatriz original después de intercambiar la tercera fila con la suma de sí misma y la primera fila multiplicada por 4:")
print(SumarFilas(A_test, 0, 2, 4))

print("\nMatriz original después de intercambiar su primera y tercera filas:")
print(IntercambiarFilas(A_test, 0, 2))
print('\n',A_test)

#Ejercicio número 2
# Programa para resolver un sistema de ecuaciones lineales mediante eliminación manual

# Definir la matriz aumentada
A = np.array([[2, 3, -1],
              [4, -1, 2],
              [3, 2, -1]], dtype=float)

b = np.array([8, 3, 5], dtype=float)

matriz_aumentada = np.hstack((A, b.reshape(-1, 1)))
M = matriz_aumentada

# Aplicar operaciones para triangularizar la matriz
print('\n',M)
M = MultiplicarFila(M,0,1/M[0,0])
print('\n',M)
M = SumarFilas(M,0,1,-M[1,0])
M = SumarFilas(M,0,2,-M[2,0])
print('\n',M)
M = MultiplicarFila(M,1,1/M[1,1])
print('\n',M)
M = SumarFilas(M,1,2,-M[2,1])
print('\n',M)
M = MultiplicarFila(M,2,1/M[2,2])
print('\n',M)
# Resolución hacia atrás
print(M[2][3])
print(len(M[0]))
x = np.zeros(len(M[0]) - 1, dtype=float)
print('\n',x[1+1:])
for i in range(len(M)-1, -1, -1):
    x[i] = M[i][-1] - np.dot(M[i][i+1:-1], x[i+1:])


print("Solución del sistema:")
print(x)
print("Solución del sistema:")
print(np.linalg.solve(A,b))

