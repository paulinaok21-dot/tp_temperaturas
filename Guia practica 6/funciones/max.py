def temmaxima(lista_temperatura):
    mayor = 0
    for elemento in lista_temperatura :
        if elemento > mayor:
            mayor = elemento
    return mayor