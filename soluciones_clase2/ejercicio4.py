"""
Implementar una función que reciba como parámetro un número entero y retorne 
la cantidad de dígitos que posee y la suma de los mismos.
"""

def digitos(numero):
    numero_texto = str(numero)
    suma = 0
    for digito in numero_texto:
        suma = suma + int(digito)
    
    return "la cantidad de digitos es: " + str(len(numero_texto)) + " .La suma es: " + str(suma)  

print(digitos(12345))
