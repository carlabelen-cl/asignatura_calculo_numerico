a=int(input("ingrese numero "))
b=int(input("ingrese numero ")) ## solicitamos dos números para calcular su MCD :D

if a > b:
    n_max= a ## Ordenamos los númeritos para saber cual es el mayor y poder ejecutar el algoritmo?
    n_min= b
else:
    n_max= b
    n_min= a

r_actual= n_max % n_min ## guarda el residuo 
r_pasado= n_min ## guarda nuestro número menor (el divisor)
## q_actual= n_max//n_min esta igual no tiene funcionalidad, quizá por ahora
## q_pasado=30 no tiene funcionalidad pero la dejo por si a caso:D
x=True ## se usa como interruptor, mientras x true entonces el mientras se ejecuta :D
while x:
    if r_actual == 0: ## si la división llego a 0 entonces encontramos nuestro MCD
        mcd= r_pasado ## muestra el último divisor que genero que la división sea 0 (ese es el MCD)
        x= False ## Lo encontró entonces terminó :D
    else:
        ##q_actual= n_min//r_pasado por lo visto no tiene funcionalidad 
        r_pasado= r_actual ## el residuo viejo toma el lugar del nuevo divisor 
        r_actual= n_min%r_pasado ## calcula el nuevo residuo 

mcm= (a*b)/mcd
print("maximo común divisor es", int(mcd)) 
print("minimo común múltiplo es", int(mcm)) 
