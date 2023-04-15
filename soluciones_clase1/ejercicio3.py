"""
1. Leer números del teclado float(input())
2. En loop. Condición de corte 0
3. Guardar en lista
4. Ordenar de mayor a menor --> sort(reverse(True))
5. Si la lista está ordenada, el último es el menor y el primero el mayor
"""

lista_numeros = []

while True:
    numero = float(input("Ingrese numero: "))
    if numero == 0:         #condición de corte. Salimos con break
        break
    lista_numeros.append(numero)

lista_numeros.sort(reverse=True)
print("El menor es: ", lista_numeros[-1])
print("El mayor es: ", lista_numeros[0])
print(lista_numeros)