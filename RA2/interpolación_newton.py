import numpy as np

cantidad_datos = int(input("Cantidad de datos: "))

lista_x = []
lista_y = []

for numero in range(cantidad_datos):
    lista_x.append(float(input(f"x{numero+1}: "))) ## lo mismo que los ejercicios anteriores 
    lista_y.append(float(input(f"y{numero+1}: ")))

tabla_diferencias = np.zeros((cantidad_datos, cantidad_datos)) ## una matriz de 0 
tabla_diferencias[:, 0] = lista_y # en todas las filas de la columna cero se distribuirá y

for columna in range(1, cantidad_datos): ## parte en 1 por que la columna 0 ya tiene las y
    for fila in range(cantidad_datos - columna): ## generará forma triangular 
        numerador = tabla_diferencias[fila + 1][columna - 1] - tabla_diferencias[fila][columna - 1] ## aca aplicamos formula 
        denominador = lista_x[fila + columna] - lista_x[fila]
        tabla_diferencias[fila][columna] = numerador / denominador ## obtenemos la tabla de diferencias finalmente c: (para cada celda)

coeficientes_newton = tabla_diferencias[0, :] ## primera fila de la tabla 

punto_a_evaluar = float(input("Valor de x a evaluar: ")) ## pedimos el valor de x 

resultado = coeficientes_newton[0] ## recorre cada coeficiente de newton
producto_acumulado = 1 ## crea la variable donde se aplicará la suma 

## evaluamos el polinomio finalmente 
for k in range(1, cantidad_datos):
    producto_acumulado = producto_acumulado * (punto_a_evaluar - lista_x[k - 1])
    resultado = resultado + coeficientes_newton[k] * producto_acumulado

print(f"P({punto_a_evaluar}) = {resultado}")