import math
## definimos las funciones :D
def f(x):
    return math.exp(x) - 3 * x

def df(x):
    return math.exp(x) - 3
## generamos la función de Newton-Raphson (ES PRACTICAMENTE LA MISMA QUE LA ANTERIOR, SOLO CAMBIA LA FUNCIÓN)
def newton_raphson(x0, tol):
    x = x0
    iteraciones = 0
    resultados = []
    while True:
        x_nuevo = x - f(x) / df(x)
        iteraciones += 1
        ea = abs((x_nuevo - x) / x_nuevo) * 100
        resultados.append((iteraciones, x_nuevo, ea))
        if ea < tol:
            break
        x = x_nuevo
    return resultados
## Y PARA ESTE LO MISMO SOLO CAMBIA LA FUNCIÓN, PERO EL ALGORITMO ES EL MISMO
def biseccion(a, b, tol):
    iteraciones = 0
    x_prev = a
    resultados = []
    while True:
        x_m = (a + b) / 2
        iteraciones += 1
        if iteraciones > 1:
            ea = abs((x_m - x_prev) / x_m) * 100
        else:
            ea = 100.0
        resultados.append((iteraciones, x_m, ea))
        if ea < tol and iteraciones > 1:
            break
        if f(a) * f(x_m) < 0:
            b = x_m
        else:
            a = x_m
        x_prev = x_m
    return resultados

tol = 0.05

## llamar la función de Newton-Raphson y bisección con los valores iniciales y la tolerancia definida
res_nr = newton_raphson(0, tol)
res_bis = biseccion(0, 1, tol)
 ## MOSTRAR LAS TABLITAS SOLICITADAS
print("--- NEWTON-RAPHSON ---")
print("i | xi | ea (%)")
for i, x_val, ea_val in res_nr: ## para imprimir la tabla de resultados de Newton-Raphson, se recorre la lista de resultados y se imprime cada iteración con su valor de xi y el error relativo porcentual
    print(f"{i} | {x_val} | {ea_val}")

print("\n--- BISECCIÓN ---")
print("i | xi | ea (%)")
for i, x_val, ea_val in res_bis: ## lo mismo que la anterior 
    print(f"{i} | {x_val} | {ea_val}")