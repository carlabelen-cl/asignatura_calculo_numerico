## algoritmo para calcular los primeros números de la secuencia de fibonacci 
lista_fibonacci = [1, 1]  # Inicializamos la lista con los dos primeros números de Fibonacci

for i in range(8): ## SE PUEDE USAR CUALQUIER NÚMERO (PERO YA TENEMOS 2 DE LA LISTA DE ARRIBA)
    siguiente_num = lista_fibonacci[-1] + lista_fibonacci[-2]  #[-1] accede al último elemento de la lista, y [-2] al penultimo y así :D
    lista_fibonacci.append(siguiente_num) ## usamos la funcion apendd para agregar el número cálculado :D

print("Los primeros 10 números de la secuencia de Fibonacci son:")
print(lista_fibonacci)

lista_de_límites= []

for i in range(1, len(lista_fibonacci)):
    límite = lista_fibonacci[i] / lista_fibonacci[i - 1]  # Calculamos el límite como el cociente del número actual y el anterior
    lista_de_límites.append(límite)

print("Límites de la secuencia de Fibonacci:")
print(lista_de_límites)

lambda_aprox = lista_de_límites[-1]

print(f"Aproximación de lambda con n={len(lista_fibonacci)}:")
print(f"λ ≈ {lambda_aprox:.10f}")