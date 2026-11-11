import math

# numero aureo
num_aureo = (1 + math.sqrt(5)) / 2

# listas principales 
lista_fibonacci = [1, 1]
lista_de_limites = []

# Bucle que genera la secuencia hasta que la división sea idéntica al numero aureo
while (lista_fibonacci[-1] / lista_fibonacci[-2]) != num_aureo:
    siguiente_num = lista_fibonacci[-1] + lista_fibonacci[-2]
    lista_fibonacci.append(siguiente_num)

# lista de límites (division entre cada termino c:)
for i in range(1, len(lista_fibonacci)):
    limite = lista_fibonacci[i] / lista_fibonacci[i - 1]
    lista_de_limites.append(limite)

# mostrar resultados
print("--- RESULTADOS ---")
print(f"Número Áureo (fórmula matemática): {num_aureo}")
print("\nSecuencia de Fibonacci generada:")
print(lista_fibonacci)
print(f"Cantidad de números de Fibonacci necesarios: {len(lista_fibonacci)}")
print("\nLista de límites:")
print(lista_de_limites)
print(f"\nAproximación final (último término de la división): {lista_de_limites[-1]}")