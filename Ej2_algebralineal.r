# Programa para resolver un sistema de ecuaciones lineales mediante eliminación manual

# Definir la matriz aumentada
A = np.array([[2, 3, -1],
              [4, -1, 2],
              [3, 2, -1]], dtype=float)

b = np.array([8, 3, 5], dtype=float)

matriz_aumentada = np.hstack((A, b.reshape(-1, 1)))
M = matriz_aumentada

# Aplicar operaciones para triangularizar la matriz
M = MultiplicarFila(...)
M = SumarFilas(...)
M = MultiplicarFila(...)
M = SumarFilas(...)
M = IntercambiarFilas(...)
M = SumarFilas(...)
M = SumarFilas(...)
print(M)


# Resolución hacia atrás
x = np.zeros(len(M[0]) - 1, dtype=float)
for i in range(len(M)-1, -1, -1):
    x[i] = M[i][-1] - np.dot(M[i][i+1:-1], x[i+1:])


print("Solución del sistema:")
print(x)
print("Solución del sistema:")
#print(np.linalg.solve(A,b))
