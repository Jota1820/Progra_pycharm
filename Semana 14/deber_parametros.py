def suma_productos (matriz):  #Creamos otra función con un parametro
    sumar = 0  # Declaramos la variable
    desc = 0
    for i in range(len(matriz)): # Cremoas un bucle for para recorrer la longitud de la matriz
        sumar +=  matriz[i][3]  #Sumamos la matriz
        desc = sumar - (descuento * sumar / 100)  # La suma restamos por el porcentaje de descuento

    return  desc  #Retornamos el descuento



def descuento_precio (producto,cantidad,precio,descuentos): #Creamos la función con 4 parametros

    subtotal = cantidad * precio  #Realizamos la multiplicacion de la cantidad por el precio
    matriz = [producto,cantidad,precio,subtotal,descuentos]  # En la matriz guardamos los elementos
    return matriz # Retornamos la matriz


descuento = int(input("Ingrese el descuento: "))  #Declaramos la variable descuento

matriz_t = []  #Creamos una lista vacia





while True :  #Creamos un bucle while para ingresar los datos
    prod = input("Ingrese el producto: ")
    cant = int(input("Ingrese la cantidad: "))
    pre = float(input("Ingrese el precio: "))
    matriz_t.append(descuento_precio(prod, cant, pre, descuento))
    decision = input("¿ Desea ingresar otro prodcuto ? ") #Preguntamos si deseamos agregar mas prodcutos
    if decision == "no":
        break  #Si coloca no se terminará la ejecución


for tabla in matriz_t:  #Imprimimos nuestra tabla
    print(tabla)
precio_final = suma_productos(matriz_t)  #Llamamos a la función y su parametro
print(f"El precio final de los productos con el descuento del {descuento}% es {precio_final}")  #Imprimimos el precio final con el descuento
