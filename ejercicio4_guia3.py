## este sigue la logica de todos los anteriores, pero con una funcion diferente :3 

def f(x):
    return ((x - 1) ** 2) * (x + 2)

def df(x):
    return 2 * (x - 1) * (x + 2) + ((x - 1) ** 2)

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

tol = 0.1
res = newton_raphson(2, tol)

print("i | xi | ea (%)")
for i, x_val, ea_val in res:
    print(f"{i} | {x_val} | {ea_val}%")

## respuesta de la primera pregunta: se le hace mas complejo llegar ya que esta esta elevada al cuadrado, de hecho le toma 7 iteraciones mas que el ejercicio anterior
## respuesta de la segunda pregunta: no se puede usar bisección por que como el 1 está dentro del elevado al cuadrado siempre dará positivo (pasará por el 0) pero continuará dando positivo entonces no fabrá la diferenciación de f(a) * f(x_m) < 0, por lo que no se puede usar bisección para este caso