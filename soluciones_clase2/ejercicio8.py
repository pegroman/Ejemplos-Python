"""
Realizar un programa que reciba como parámetro el radio de un círculo y 
retorne su diámetro y su perímetro. Implementar utilizando funciones.
"""
import math #para usar PI

def diametro_perimetro_circulo(radio):
    diametro = 2 * radio
    perimetro =  2 * math.pi * radio
    return "El diametro es: " + str(diametro) +  ". El perimetro es: " + str(perimetro)

print(diametro_perimetro_circulo(5))