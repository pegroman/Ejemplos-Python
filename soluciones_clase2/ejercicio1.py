"""
Defina una función que reciba una palabra y retorne la cantidad de vocales 
que contiene.  
    a.Implemente la solución con  una función iterativa.
    b.Implemente la solución con una función recursiva.
"""

#solución iterativa!
def cantidad_vocales(palabra):
    contador = 0
    for letra in palabra.lower():
        if letra in "aeiou":
            contador = contador + 1
    
    return contador

#print(cantidad_vocales("araujo"))

#solucion recursiva!
def contar_vocales_recursivo(palabra, tamanio_palabra,contador):
    #caso base:
    if tamanio_palabra == -1:
        return contador
    
    #caso recursivo:
    if palabra[tamanio_palabra] in "aeiou":
        contador = contador + 1

    return contar_vocales_recursivo(palabra, tamanio_palabra - 1, contador)

#palabra="araujo"
#print(contar_vocales_recursivo(palabra, len(palabra)-1,0))
