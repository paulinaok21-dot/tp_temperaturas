def ordenar_lista(lista_temperatura):
    for i in range(1, len(lista_temperatura)):
        for j in  range(0,len(lista_temperatura-1)):
            if lista_temperatura[j] > lista_temperatura[j+1]:
                aux = lista_temperatura[j]
                lista_temperatura[j]=lista_temperatura[j+1]
                lista_temperatura[j+1]=aux
    return(lista_temperatura)