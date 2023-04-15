"""
1. Pedir por teclado nombre marca y cantidad vendido.
2. Guardar en un diccionario. 
    2a. Si existe en la estructura, acutualizar la cantidad.
    2.b. Si no existe, agregar entrada nueva al diccionario.
3. Tiene que ser en loop. While con condición de corte "EXIT".
4. Agregar en un set() las marcas. Para que no queden marcas repetidas.
5. Imprimir el diccionario.
"""

diccionario_marcas = dict()
marcas_unicas = set()
while True:
    marca = input("Ingrese marca. Para salir EXIT: ")
    if marca == "EXIT":
        break
    marcas_unicas.add(marca)
    cantidad = int(input("Ingrese cantidad: "))

    if marca in diccionario_marcas:
        diccionario_marcas[marca] += cantidad
    else:
        diccionario_marcas[marca] = cantidad

print("La lista de marcas únicas es: ")
print(marcas_unicas)

print("El listado de productos por marcas es: ")
print(diccionario_marcas)


