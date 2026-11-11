import math

x = 5 # -x = -5 / x= 5
n_terminos = 20
val_verdadero = math.exp(-5)   # Calcular el valor verdadero de e^-5 usando la función exp de la biblioteca math

# Variables para guardar las sumas acumuladas
suma_m1 = 0
denominador_m2 = 0

for i in range(n_terminos): # Primera forma de calcular e^-x usando la serie de Maclaurin
    termino_m1 = ((-1)**i) * (x**i) / math.factorial(i) # -1 elevado a i, multiplicado por x elvado a i y debido por el factorial de i c: 
    suma_m1 += termino_m1  # Lo sumamos al total de la primera formula 
    
    # Segunda forma de calcular e^-x usando la serie de Maclaurin
    termino_m2 = (x**i) / math.factorial(i) # lo mismo que arriba pero en positivo 
    denominador_m2 += termino_m2  # sumamos todo al denominador 
    resultado_m2 = 1 / denominador_m2  # ahora dividimos 1 entre el denominador para obtener el resultado de la segunda formula
    
    # Calcular los errores 
    error_m1 = abs((val_verdadero - suma_m1) / val_verdadero) * 100
    error_m2 = abs((val_verdadero - resultado_m2) / val_verdadero) * 100
    
    print(f"Término {i+1}:")
    print(f"  Método 1 = {suma_m1} | Error = {error_m1}%")
    print(f"  Método 2 = {resultado_m2} | Error = {error_m2}%")