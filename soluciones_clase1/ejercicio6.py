"""
1. Pedir un año por teclado --> int(input())
2. Verificar todos los casos:
    2a. Si es divisible por 4, ir al paso 2b. Caso contrario, paso 2e.
    2b. Si es divisible por 100, ir al paso 2c. Caso contrario, paso 2d.
    2c. Si es divisible por 400, ir al paso 2d. Caso contrario, paso 2e.
    2d. Es una año bisiesto.
    2e. No es un año bisiesto.
"""

anio = int(input("Ingrese un año: "))

if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
    print(anio," es bisiesto")
else:
    print(anio," NO es bisiesto")
