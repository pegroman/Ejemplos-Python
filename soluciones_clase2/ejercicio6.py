"""
Escriba una función recursiva que reciba una lista de apellidos y 
retorne si existe o no un apellido dado en la lista. 
"""

def buscar_apellido(lista_apellidos, apellido, contador, existe):

    if contador == -1 or existe == True:
        return existe
    
    if lista_apellidos[contador] == apellido:
        existe = True

    return buscar_apellido(lista_apellidos, apellido, contador - 1, existe)

lista = ["amaranto", "eustaqui", "perez", "piriz", "arlt"]
print(buscar_apellido(lista, "perez", len(lista) - 1, False))
