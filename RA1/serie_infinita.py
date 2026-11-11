## hacer la sumatoria de 1/i a la cuarta 
import math 
serie_infinita_1000 = []

n = int(input("Ingrese el número de términos para la sumatoria: "))

for i in range(1, n + 1):
    sumatoria = sum(1 / (j ** 4) for j in range(1, i + 1))
    serie_infinita_1000.append(sumatoria)

print("La sumatoria de 1/i^4 hasta", n, "términos es:", serie_infinita_1000[-1])

constante = (math.pi ** 4) / 90

Ea= abs(constante - serie_infinita_1000[-1])
Er= Ea / constante
Ep= Er * 100 

print(f"El error porcentual para {n} términos es: {Ep}%")
print(f"El valor de la sumatoria es: {serie_infinita_1000[-1]} y el valor de la constante es: {constante}")
print(f"El error absoluto es: {Ea} y el error relativo es: {Er}")

## calcular lo mismo pero a la inversa 
serie_infinita_inversa = []

for a in range(n, 0,-1):
    sumatoria_inversa = sum(1 / (j ** 4) for j in range(1, a + 1))
    serie_infinita_inversa.append(sumatoria_inversa) 
print("La sumatoria inversa de 1/i^4 hasta", n, "términos es:", serie_infinita_inversa[0])

Ea_inverso= abs(constante - serie_infinita_inversa[0])
Er_inverso= Ea_inverso / constante
Ep_inverso= Er_inverso * 100 

print(f"El error porcentual para {n} términos es (inverso): {Ep_inverso}%")
print(f"El valor de la sumatoria es (inverso): {serie_infinita_inversa[0]} y el valor de la constante es: {constante}")
print(f"El error absoluto es (inverso): {Ea_inverso} y el error relativo es (inverso): {Er_inverso}")