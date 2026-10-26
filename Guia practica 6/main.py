from funciones.temperatura import *
from funciones.max import *
from funciones.min import *
from funciones.mayor import *
from funciones.contar import*
from funciones.vertem import *
lista_temperatura = []
def menu():
    print("1-agregar temperatura")
    print("2- buscar mayor")
    print("3-buscar menor")
    print("4-calcular promedio")
    print("5-temperaturas mas grandes a 20°")
    print("6-elegir cantidad de temperaturas")
    print("7-ver temperaturas")
    print("8-ordenar lista")
    print("9-salir")
op = int(input("ingrese la opcion que desee elegir: "))
return op
while True:
    res = menu()
    if op == 1:
        c=int(input("ingrese la temperatura"))
        lista.append(c)
    elif op == 2:
        valor = temmaxima(lista_temperatura)
        print(valor)     
    elif op == 3:
        valor2 = temminima(lista_temperatura)
        print(valor2)
    elif op == 4:
        res= calcularpromedio(lista_temperatura)
        print(res)
    elif op == 5:
        res1 = veinte(lista_temperatura)
        print(res1)
    elif op == 6:
        pre = int(input("ingrese a que temperatura tiene que ser igual: "))
        res2 = contar(lista_temperatura,pre)
        print(res2)
    elif op == 7:
        res3 = ver_temperatura(lista_temperatura)
        print(res3)
    elif op == 8:
        res4 = ordenar_lista(lista_temperatura)
    elif op == 9:
        break