class Persona():

    def __init__(self, unNombre, unaEdad, unDni):
        self.__nombre = unNombre
        self.__edad = unaEdad
        self.__dni = unDni

    def getNombre(self):
        return self.__nombre

    def setNombre(self, unNombre):
        self.__nombre = unNombre

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def getDni(self):
        return self.__dni

    def setDni(self, dni):
        self.__dni = dni

    def __str__(self):
        cadena = self.getNombre() + " (" + str(self.getEdad()) + ") " + self.getDni()
        return cadena

###aplicacion####
lista_personas=[]
corte = input("Desea ingresar datos de persona s/n: ")
while corte != "n":
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    dni = input("DNI: ")
    una_persona = Persona(nombre,edad,dni)
    lista_personas.append(una_persona)
    corte = input("Desea ingresar datos de persona s/n: ")

contador = 0
for persona in lista_personas:
    contador += 1
    print(str(contador) +") " + str(persona))