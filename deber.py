#Declaramos nuestra lista 3D


tempe_ciudades = [
    [  #Ciudad 1
    [25,26,13,24,11,12,12],
    [20,15,10,17,11,14,15],
    [25,29,28,11,12,26,17],
    [19,16,19,9,27,29,18]
],
    [ #Ciudad 2
    [22,21,17,8,19,23,22],
    [27,23,23,25,29,27,17 ],
    [24,26,12,27,10,12,15],
    [21,15,12,25,25,24,17]
    ],
[ #Ciudad 3
    [17,15,14,27,17,11,29],
    [26,17,13,28,27,29,27],
    [30,11,12,14,26,27,25],
    [18,23,31,26,26,15,19]
    ]
]

#Declaramos las variables semana,día
semana = 1
dia = 0

suma = 0



#Creamos los bucle for para recorrer nuestra lista de temepraturas
for i in range(len(tempe_ciudades)): #Recorremos toda la lista
    if i == semana: #Creamos una condición para comparar si la variable semana es igual al recorrido de nuestra iteración i
        for j in range(len(tempe_ciudades[i])): # Recorremos las semanas dentro de ciudades
            if j == dia :#Creamos una condición para comparar si la variable dias es igual al recorrido de nuestra iteración j
                 promedio = 0 #Iniciamos el promedio en 0
                 for k in range(len(tempe_ciudades[i][j])):  #Recorremos los numeros dentro de ciudades y semanas.
                    suma+= tempe_ciudades[i][j][k]  #Sumamos las temperaturas
                    promedio = suma / len(tempe_ciudades[i][j]) #Calculamos el promedio y dividimos para el conteo de nuestras lista en i y j

                 print(f"El promedio de la temperatura de la ciudad {semana} de la semana {dia} es {promedio}")  #Imprimimos el promedio