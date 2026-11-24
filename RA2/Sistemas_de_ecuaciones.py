import numpy as np

tamano = int(input("Tamaño del sistema (2 o 3): "))

matriz_A = np.zeros((tamano, tamano)) # se crea una matriz de ceros
vector_b = np.zeros(tamano) # se crea un vector de 0 , si tamaño = 2 entonces [0,0]

for fila in range(tamano): ## hacemos doble ciclo for para poder crear la matriz 
    for columna in range(tamano):
        matriz_A[fila][columna] = float(input(f"Coeficiente A[{fila+1}][{columna+1}]: ")) # se solicita al usuario que rellene los términos de la matriz 
    vector_b[fila] = float(input(f"Término independiente b[{fila+1}]: ")) # este es el vector de los resultados de la matrix 

determinante_A = np.linalg.det(matriz_A)

if abs(determinante_A) < 1e-12: ## ¿El determinante es casi 0? 
    print("El sistema no tiene solución única")
else:
    soluciones = [] ## lista de soluciones 
    for columna in range(tamano):
        matriz_modificada = matriz_A.copy() ## copiamos la matriz 
        matriz_modificada[:, columna] = vector_b ## todas las filas de esa columna pon el valor de b 
        soluciones.append(np.linalg.det(matriz_modificada) / determinante_A) ## calculamos Det(Ai)/DetA

    for posicion, valor in enumerate(soluciones):
        print(f"x{posicion+1} = {valor}") ## acá se imprime el x1, x2, etc 