"""
Escriba una función recursiva que reciba un número y una lista de números y 
retorne la cantidad de veces que dicho número aparece en la lista. 
"""

def numero_repetido(lista, numero, contador, cantidad):
    if contador == -1:
        return cantidad

    if lista[contador] == numero:
        cantidad = cantidad + 1
    
    return numero_repetido(lista, numero, contador - 1, cantidad)

lista = [4,2,3,4,5,2,3]
print(numero_repetido(lista, 3, len(lista) - 1, 0))