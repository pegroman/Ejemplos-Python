"""
1. Leer numero desde teclado. usar int(input()) y multiplicar por 365
2. pasar el número a string --> str(numero)
3. for con range (longitud_cadena -1, -1, -1)
"""

numero = int(input("Ingrese un numero entero: ")) * 365
numero_string = str(numero)

desde = len(numero_string) - 1
hasta = -1
con_paso = -1
for indice in range(desde,hasta,con_paso):
    print(numero_string[indice])