import matplotlib.pyplot as plt
import numpy as np

# aca defino la funcion f(x)
def funcion(x):
    return (0.8 - 0.3 * x) / x

# despejando a mano nos da 0.8 / 0.3
valor_verdadero = 0.8 / 0.3
print(f"--- Parte a) Valor verdadero analítico: x = {valor_verdadero} ---\n")


# uso valores entre 0.5 y 4.0 para ver el corte
x_valores = np.linspace(0.5, 4.0, 200)
y_valores = funcion(x_valores)

plt.figure(figsize=(8, 5))
plt.plot(x_valores, y_valores, label=r"$f(x) = \frac{0.8 - 0.3x}{x}$", color="blue", lw=2)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Gráfico de f(x)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()


# limites que nos da la guia
limite_inferior = 1.0
limite_superior = 3.0

aproximacion_anterior = None

# reviso si hay cambio de signo entre 1 y 3
if funcion(limite_inferior) * funcion(limite_superior) < 0:
    # solo 3 vueltas como pide el ejercicio
    for numero_iteracion in range(1, 4):
        # aplico la formula de la recta de falsa posicion
        punto_interseccion = limite_superior - (funcion(limite_superior) * (limite_inferior - limite_superior)) / (funcion(limite_inferior) - funcion(limite_superior))
        
        # aca calculo el error aproximado (ea) desde la segunda vuelta
        if aproximacion_anterior is not None:
            error_aproximado_porcentual = abs((punto_interseccion - aproximacion_anterior) / punto_interseccion) * 100
        else:
            error_aproximado_porcentual = float('inf')
            
        # aca calculo el error verdadero (et) comparando con el valor analitico de la parte a
        error_verdadero_porcentual = abs((valor_verdadero - punto_interseccion) / valor_verdadero) * 100
        
        print(f"Iteración {numero_iteracion}: a = {limite_inferior}, b = {limite_superior}, c = {punto_interseccion}")
        print(f"   f(c) = {funcion(punto_interseccion)}")
        print(f"   Error Aproximado (ea) = {error_aproximado_porcentual}%")
        print(f"   Error Verdadero (et)  = {error_verdadero_porcentual}%\n")
        
        # ver para que lado achicamos el intervalo
        if funcion(limite_inferior) * funcion(punto_interseccion) < 0:
            limite_superior = punto_interseccion
        else:
            limite_inferior = punto_interseccion
            
        
        aproximacion_anterior = punto_interseccion

    print(f"Resultado final Falsa Posición tras 3 vueltas: c = {punto_interseccion}")
else:
    print("No hay cambio de signo entre a y b")