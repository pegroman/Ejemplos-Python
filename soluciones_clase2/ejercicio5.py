"""
Escribir un programa que genere aleatoriamente 100 números reales, 
los almacene en una lista, y luego los muestre ordenados de menor a mayor. 
Obligatorio utilizar funciones.
"""
import random

def generar_aleatorios(cantidad):
    lista  = []
    for num_aleatorio in range(0,cantidad):
        lista.append(random.random())
    return lista

def ordenar_lista_numeros(lista_numeros):
    lista_numeros.sort()
    return lista_numeros

numeros = generar_aleatorios(100)
print(numeros)
print(ordenar_lista_numeros(numeros))