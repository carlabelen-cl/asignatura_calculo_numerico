cantidad_datos = int(input("Cantidad de datos: ")) #pedimos la cantidad de datos 

lista_x = [] # creamos listas para que exista (x,y) 
lista_y = []

for numero in range(cantidad_datos): 
    lista_x.append(float(input(f"x{numero+1}: "))) # solicitamos al usuario cada par x,y 
    lista_y.append(float(input(f"y{numero+1}: ")))

suma_x = sum(lista_x) # Hacemos cada suma 
suma_y = sum(lista_y)
suma_xy = sum(x * y for x, y in zip(lista_x, lista_y)) ## aca es la suma de la multiplicación de xy
suma_x_cuadrado = sum(x ** 2 for x in lista_x)

# aplicamos fórmula 
pendiente = (cantidad_datos * suma_xy - suma_x * suma_y) / (cantidad_datos * suma_x_cuadrado - suma_x ** 2)
intercepto = (suma_y - pendiente * suma_x) / cantidad_datos

# finalmente entregamos la recta a partir de los datos entregados 
print(f"Recta: y = {pendiente} x + {intercepto}")