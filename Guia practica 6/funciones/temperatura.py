def calcularpromedio(lista:list):
    suma= 0
    contador = 0
    for elemento in lista:
        suma += elemento
        contador += 1
    promedio = suma/contador
    return promedio