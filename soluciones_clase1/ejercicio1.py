""" 1. Leer datos del teclado
    2. Tiene que ser en loop
    3. Para cortar el loop la condición es ingresar la cadena vacía ""
    4. Calcular la longitud de la cadena con len()
    5. variable para ir sumando las diferentes longitudes
    7. variable contador para contar la cantidad de elementos que se ingresan
    6. Fuera del loop, imprimir promedio
"""

suma = 0
contador_palabras = 0

print("Ingrese un string. Vacío para salir.")
palabra = input("Ingrese cadena: ")

while palabra != "":
    contador_palabras = contador_palabras + 1
    longitud = len(palabra)
    suma = suma + longitud
    palabra = input("Ingrese un string. Vacio para salir.")

promedio = suma / contador_palabras
print("El promedio de las longitudes es: ", promedio)
