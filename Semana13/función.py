def calcular_prom  (temp):
    promedios = {}

    for ciudad, temperaturas in temp.items():
        promedio = sum (temperaturas) / len(temperaturas)
        promedios [ciudad] = promedio
    return promedios

#Ejemplo de uso

datos = {
"Quito": [20, 22, 21, 23],
"Guayaquil": [25, 26, 27, 28],
"Cuenca": [18, 17, 19, 20]

}

print(calcular_prom(datos))