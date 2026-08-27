numero = int(input("Ingrese un número: "))

if numero > 1:
    es_primo = True
    
    # Comprobamos si tiene algún divisor desde 2 hasta numero - 1
    for i in range(2, numero):
        if numero % i == 0:  # Si el resto es 0, no es primo
            es_primo = False
            break  # Salimos del bucle apenas encontramos un divisor

    if es_primo:
        print("El número es primo")
    else:
        print("El número no es primo")
else:
    print("El número no es primo")