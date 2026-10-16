import math
## en este ejercicio adjuntamos los dos métodos para hacer la comparación de porque el bisección es mejor lo que se observará en la tabla 
def f(x):
    return math.atan(x)

def df(x):
    return 1 / (1 + x**2)

def newton_raphson(x0, pasos):
    x = x0
    resultados = []
    for i in range(1, pasos + 1):
        x_nuevo = x - f(x) / df(x)
        ea = abs((x_nuevo - x) / x_nuevo) * 100
        resultados.append((i, x_nuevo, ea))
        x = x_nuevo
    return resultados

def biseccion(a, b, pasos):
    iteraciones = 0
    x_prev = a
    resultados = []
    for i in range(1, pasos + 1):
        x_m = (a + b) / 2
        iteraciones += 1
        if iteraciones > 1:
            ea = abs((x_m - x_prev) / x_m) * 100
        else:
            ea = 100.0
        resultados.append((iteraciones, x_m, ea))
        if f(a) * f(x_m) < 0:
            b = x_m
        else:
            a = x_m
        x_prev = x_m
    return resultados

res_nr1 = newton_raphson(1, 4)
res_nr15 = newton_raphson(1.5, 4)
res_bis = biseccion(-1, 2, 4)

print("NEWTON-RAPHSON (x0 = 1)")
print("i | xi | ea (%)")
for i, x_val, ea_val in res_nr1:
    print(f"{i} | {x_val} | {ea_val}%")

print("\nNEWTON-RAPHSON (x0 = 1.5)")
print("i | xi | ea (%)")
for i, x_val, ea_val in res_nr15:
    print(f"{i} | {x_val} | {ea_val}%")

print("\nBISECCIÓN en [-1, 2]")
print("i | xi | ea (%)")
for i, x_val, ea_val in res_bis:
    print(f"{i} | {x_val} | {ea_val}%")

## cuando imprimimos el error relativo porcentual de la primera iteración del método de bisección 
## ya es menor que las iteraciones del método de Newton-Raphson, por lo que podemos concluir que el método de bisección es más eficiente en este caso.