import numpy as np

cantidad_datos = int(input("Cantidad de datos: ")) ## solicitamos la cantidad de datos 

lista_x = [] # creamos las listas 
lista_y = []

for numero in range(cantidad_datos): # y por cada dato pedimos el (x,y) 
    lista_x.append(float(input(f"x{numero+1}: ")))
    lista_y.append(float(input(f"y{numero+1}: ")))

vector_x = np.array(lista_x) ## convertimos nuestras listas a vectores para poder trabajar matricialmente
vector_y = np.array(lista_y)

matriz_vandermonde = np.vander(vector_x, increasing=True) # creamos la matriz y con increasing se va generando el x^1, x^2, etc 
coeficientes = np.linalg.solve(matriz_vandermonde, vector_y) #utilizamos una función de álgebra líneal 
## la cual hace el A*x= b (dónde b son los resultados conocidos, en este caso los y, y la x serían los a0, a1, a2, etc)

print("Polinomio: P(x) = a0 + a1 x + a2 x^2 + ...")
for potencia, coeficiente in enumerate(coeficientes):
    print(f"a{potencia} = {coeficiente}") ## esta sección mostrará cada a0, a1, a2, etc 

## aqui evaluamos nuestro polinomio resultante c: (le entregamos un x y nos dará el resultado)
punto_a_evaluar = float(input("Valor de x a evaluar: "))
resultado = sum(coeficiente * punto_a_evaluar ** potencia for potencia, coeficiente in enumerate(coeficientes))
print(f"P({punto_a_evaluar}) = {resultado}")