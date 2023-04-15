"""
1. Pedir dos palabras por teclado --> input()
2. Para verificar si son palíndromos entre ellas se puede
    inverter el orden de la segunda palabra.
    Si la palabra uno es igual a la palabra 2 invertida, es palíndromo
"""

#Ingreso de palabras
palabra1 = input("Ingrese primera palabra: ").lower()
palabra2 = input("Ingrese segunda palabra: ").lower()

#caso A, recorriendo cada palabra
#Podemos recorrer la palabra 2 en sentido contrario e ir comparando.

es_palindromo = True
indice = -1
for letra1 in palabra1:
    if letra1 != palabra2[indice]:
        es_palindromo = False
        break
    else:
        indice = indice - 1

if es_palindromo:
    print("Ambas palabras son palíndromos")
else:
    print("No son palíndromos")

#caso B, usando funciones predefinidas de python
#Para invertir un string o lista se puede utilizar el operador slicing [::-1]

palabra2_invertida = palabra2[::-1]

if palabra1 == palabra2_invertida:
    print("Son palíndromas entre sí.")
else:
    print("No son palíndromas.")
    