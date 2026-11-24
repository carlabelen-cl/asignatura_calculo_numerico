cantidad_datos = int(input("Cantidad de datos: ")) ## hacemos lo mismo que en los códigos anteriores 

lista_x = []
lista_y = []

for numero in range(cantidad_datos):
    lista_x.append(float(input(f"x{numero+1}: ")))
    lista_y.append(float(input(f"y{numero+1}: "))) ## hasta aquí es lo mismo 

punto_a_evaluar = float(input("Valor de x a evaluar: ")) ## solicitamos el X que queremos evaluar en el polinomio resultante por lagrange :D

resultado = 0 ## creamos el resultado inicial en 0 

for i in range(cantidad_datos): #lista y 
    base_lagrange = 1 ## creamos lo que será cada L0, L1, L2, etc 
    for j in range(cantidad_datos): 
        if j != i: ## J distinto de I 
            base_lagrange = base_lagrange * (punto_a_evaluar - lista_x[j]) / (lista_x[i] - lista_x[j]) ## aplicamos fórmula 
    resultado = resultado + lista_y[i] * base_lagrange ## este es cada y0*L0, y1*L1 etc

print(f"P({punto_a_evaluar}) = {resultado}") ## resultado de nuestro punto a evaluar con lagrange :D 