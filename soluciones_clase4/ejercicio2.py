""" 
Nota: la mejor forma de resolver este ejercicio, en realida es 
sobreescribiendo el metodo imprimirDatos(). Mas que nada en la parte final
del ejercicio.
"""

from ejercicio1 import Persona, Alumno

lista=[]
corte = input("Desea ingresar datos s/n: ")
while corte != "n":
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    dni = input("DNI: ")
    clase = input("Desea ingresar Persona o Alumno A/P: ")
    if clase == "A":
        promedio = input("Promedio: ")
        un_alumno = Alumno(nombre,edad,dni,promedio)
        lista.append(un_alumno)
    if clase == "P":
        una_persona = Persona(nombre,edad,dni)
        lista.append(una_persona)
    corte = input("Desea ingresar datos s/n: ")

contador = 0
for item in lista:
    contador += 1
    if isinstance(item,Alumno):
        print("ALUMNO " + str(contador) +") " + item.imprimirDatos())
    else:
        print("PERSONA " + str(contador) +") " + item.imprimirDatos())