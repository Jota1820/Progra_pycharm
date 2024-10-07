#Visualizar texto

entrada = open("my_notes.txt","r") #Abrimos el archivo txt y colocamos r de que nos va a permitir leer

visualizar = entrada.readline()  #Creamos el metodo readline que nos indica la primera linea
print(visualizar)  #Imprimimos la primera linea

#Creamos un bocle for que recorrera las demas lineas
try:
    for linea in entrada:

        print(linea)  #Imprimimos

finally:
    entrada.close() #Cerramos el archivo