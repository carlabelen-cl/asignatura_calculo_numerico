valor_verdadero = 0.69314718056 ## usamos el aproximado que entrega la guía 

suma = 0.0 #inicializamos la variable suma 

for n in range(1, 9): ## del 1 al 10
    termino = ((-1) ** (n + 1)) / n ##aplicamos la formula
    suma += termino ## sumamos termino por termino de la formula
    if n >= 4: ## solo piden de S4 a S8 asi que hacemos la comparacion a partir de n=4
        error_abs = abs(valor_verdadero - suma) ## este iterará y se mostrará por cada iteración :D
        error_rel_porcentual = abs(error_abs / valor_verdadero) * 100
        print(f"S_{n} = {suma}")
        print(f"  Error absoluto = {error_abs:.8e}")
        print(f"  Error relativo porcentual = {error_rel_porcentual}%\n")
## error relativo porcentual menos a 1e-6 
tol = 1e-6
n = 1
suma_c = 0.0

while True:
    termino = ((-1) ** (n + 1)) / n
    suma_c += termino
    error_abs = abs(valor_verdadero - suma_c)
    if error_abs < tol:  ## cuaando nuestro error abs sea menos a 1e-6 entonces se rompe el ciclo :D
        break
    n += 1 # cuantas iteraciones necesitamos 

print(f"Terminos necesarios para un error absoluto menor a 10^-6: {n}")