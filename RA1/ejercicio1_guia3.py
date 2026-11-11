
## definimos la primera función
def f(x):
    return x**3 - 20
## definimos la derivada de la función 
def df(x):
    return 3 * x**2
## generamos la función de Newton-Raphson
def newton_raphson(x0, tol):
    x = x0 ## actualiza el x
    iteraciones = 0 ## comienza en 0 
    print("Newton-Raphson:")
    while True: ## mientras sea verdadero
        x_nuevo = x - f(x) / df(x) ## ejecutamos la formula de Newton-Raphson
        iteraciones += 1 ## suma una iteración cada que se ejecute el ciclo
        ea = abs((x_nuevo - x) / x_nuevo) * 100 ## calculamos el error relativo porcentual en cada iteración
        print(f"Iteración {iteraciones}: x = {x_nuevo}, ea = {ea}%")
        if ea < tol: ## cuando el error relativo porcentual sea menor que la tolerancia, se rompe el ciclo
            break 
        x = x_nuevo 
    return x_nuevo, iteraciones ## aqui nos devuelve el valor de la raíz y el número de iteraciones que se realizaron

## algoritmo de bisección con función 
def biseccion(a, b, tol):
    iteraciones = 0
    x_prev = a ### inicializamos x_prev con el valor de a
    print("\nBisección:")
    while True: ## mientras sea verdadero ejecutamos el ciclo
        x_m = (a + b) / 2
        iteraciones += 1 ## lo mismo que el anterior, suma una iteración cada que se ejecute el ciclo
        if iteraciones > 1: # cuando la iteracion sea mayor a 1 (osea la segunda) calcula el error relativo porcentual
            ea = abs((x_m - x_prev) / x_m) * 100 
        else:
            ea = 100.0 #sino el error al principio es 100%
        print(f"Iteración {iteraciones}: x = {x_m}, ea = {ea}%")
        if ea < tol and iteraciones > 1: ## cuando el error relativo porcentual sea menor que la tolerancia y la iteración sea mayor a 1, se rompe el ciclo
            break
        if f(a) * f(x_m) < 0: ## si el producto de f(a) y f(x_m) es menor que 0, entonces la raíz está en el intervalo [a, x_m]
            b = x_m # actualizamos b con el valor de x_m
        else:
            a = x_m # sino, la raíz está en el intervalo [x_m, b], entonces actualizamos a con el valor de x_m
        x_prev = x_m 
    return x_m, iteraciones ## devuelve el valor de la raíz y el número de iteraciones que se realizaron

tol = 0.005 ## la tolerancia es 0.005

raiz_nr, iter_nr = newton_raphson(3, tol) # llamamos a la función de Newton-Raphson con un valor inicial de 3 y la tolerancia definida
raiz_bis, iter_bis = biseccion(2, 3, tol) # llamamos a la función de bisección con un intervalo [2, 3] y la tolerancia definida

print(f"\nResultados finales:")
print(f"Newton-Raphson: raíz ≈ {raiz_nr} en {iter_nr} iteraciones")
print(f"Bisección: raíz ≈ {raiz_bis} en {iter_bis} iteraciones")