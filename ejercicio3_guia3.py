import math
## definimos las funciones :D
def f(x):
    return math.log(x) + x - 2

def df(x):
    return (1 / x) + 1

## aca hacemos la misma función pero con ciclo for ya que nos pide un límite de iteraciones, en este caso 4
def newton_raphson(x0, max_iter):
    x = x0
    resultados = []
    for i in range(1, max_iter + 1): ## el +1 es porque range no incluye el último valor, entonces para que llegue a 4 iteraciones le sumamos 1
        x_nuevo = x - f(x) / df(x)
        ea = abs((x_nuevo - x) / x_nuevo) * 100 ## esto es lo mismo de las veces anteriores
        resultados.append((i, x_nuevo, ea))
        x = x_nuevo
    return resultados
 ## definimos las variables que entraran dentro de la función 
x0 = 1
max_iter = 4

res = newton_raphson(x0, max_iter)

print("i | xi | ea (%)") ## hacemos la tabla de resultados, donde i es el número de iteración, xi es el valor de la raíz aproximada y ea es el error relativo porcentual
for i, x_val, ea_val in res: ## res es donde se guardan los resultados de cada iteración, y se recorre para imprimirlos en la tabla
    print(f"{i} | {x_val} | {ea_val}%")

ea_final = res[-1][2] ### esto es para obtener el error relativo porcentual de la última iteración, que es el último elemento de la lista res, y el tercer elemento de la tupla (i, x_nuevo, ea) que es el error relativo porcentual

n_cifras = 1 ### esto es para calcular el número de cifras significativas garantizadas al final, que se calcula con la fórmula 0.5 * (10 ** (2 - n_cifras)) >= ea_final, donde n_cifras es el número de cifras significativas y ea_final es el error relativo porcentual de la última iteración
while 0.5 * (10 ** (2 - n_cifras)) >= ea_final:
    n_cifras += 1

n_cifras -= 1 ## esto es para restarle 1 al número de cifras significativas, ya que el bucle while termina cuando la condición deja de cumplirse, entonces se le resta 1 para obtener el número de cifras significativas garantizadas al final
print(f"\nCifras significativas garantizadas al final: {n_cifras}")