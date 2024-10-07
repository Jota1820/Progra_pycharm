#Creamos el archivo

entrada = open("my_notes.txt","w")  #Creamos la carpeta y colocamos write

try:
    #Con ayuda del metodo write escribirmos texto
    entrada.write("En la semana 16 \n")
    entrada.write("Vamos aprender a escribir y leer archivos en python\n")
    entrada.write("Esta es la linea 3 ")

finally:
    entrada.close()  #Cerramos el archivo