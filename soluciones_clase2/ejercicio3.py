"""
Retome el ejercicio 1. Defina un módulo para guardar la función definida 
en ese inciso. Luego  desarrolle una aplicación donde importe ese módulo e 
implemente un programa que reciba una sucesión de palabras y arme un 
diccionario indicando para cada palabra la cantidad de vocales que posee. 
Imprima el diccionario. 

Para esto va a ser necesario utilizar el archivo ejercicio1.py como modulo.
Con un simple import ejercicio1 debería funcionar.
Comenta cualquier print del archivo ejercicio1.py
"""

from ejercicio1 import *

palabras = ["hola", "camion", "araujo", "arlt", "dianno"]
diccionario = dict()
for palabra in palabras:
    diccionario[palabra] = contar_vocales_recursivo(palabra, len(palabra) - 1, 0)

print(diccionario)
