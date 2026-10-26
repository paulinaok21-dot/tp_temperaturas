def temminima(lista_temperatura):
    minimo = 99999999999
    for elemento in lista_temperatura :
        if elemento < minimo:
            minimo = elemento
    return minimo