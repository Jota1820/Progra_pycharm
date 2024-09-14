temperaturas_ciudades = [  #Creamos nuestra lista
        [  # Ciudad 1
            [25, 26, 13, 24, 11, 12, 12],
            [20, 15, 10, 17, 11, 14, 15],
            [25, 29, 28, 11, 12, 26, 17],
            [19, 16, 19, 9, 27, 29, 18]
        ],
        [  # Ciudad 2
            [22, 21, 17, 8, 19, 23, 22],
            [27, 23, 23, 25, 29, 27, 17],
            [24, 26, 12, 27, 10, 12, 15],
            [21, 15, 12, 25, 25, 24, 17]
        ],
        [  # Ciudad 3
            [17, 15, 14, 27, 17, 11, 29],
            [26, 17, 13, 28, 27, 29, 27],
            [30, 11, 12, 14, 26, 27, 25],
            [18, 23, 31, 26, 26, 15, 19]
        ]
    ]

for i in temperaturas_ciudades:
    print(i)
def calcular_prom  (temp,ciudad,semana):  #Definimos nuestra funcion con tres parametros


    suma = 0  #Declaramos nuestra variable suma y la inicializamos en cero
    promedio = 0 #Delcaramos nuestra variable promedio y la inicializamos en cero
    for i in range(len(temp[ciudad][semana])):  #Creamos un for que va a recorrer la longitu de nuestra lista y las posiciones que indicamos
        suma += temp[ciudad][semana][i] # Sumamos dentro de la posición que elejimos en ciudad y semana.

    promedio = suma / len(temp[ciudad][semana]) #Calculamos el promedio que es la suma dividio para la longitud de la posición ciudad y semana
    return  promedio  #Retornamos nuestro promedio
ciudad_usu = int(input("Ingrese la ciudad: ")) #Declaramos la variable para que el usuario ingrese
semana_usu = int(input("Ingrese la semana: ")) #Declaramos la variable para que el usuario ingrese


cal_ciudades = calcular_prom(temperaturas_ciudades,ciudad_usu,semana_usu)  #Guardamos en una variable la funcion con los parametros, dentro de los parametros colocamos la variable ciudad
                                                                           #y semana que es colocada por el usuario
print(f"La ciudad {ciudad_usu} en la semana {semana_usu}  tiene un promedio de {cal_ciudades: .2f}") #Imprimimos



