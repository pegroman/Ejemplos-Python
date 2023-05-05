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
    
    def imprimirDatos(self):
        cadena = self.getNombre() + " (" + str(self.getEdad()) + ") " + self.getDni()
        return cadena

class Alumno(Persona):

    def __init__(self,nombre,edad,dni,promedio):
        super().__init__(nombre,edad,dni)
        self.__promedio = promedio

    def getPromedio(self):
        return self.__promedio

    def setPromedio(self,promedio):
        self.__promedio = promedio
    
    def imprimirDatos(self):
        return super().imprimirDatos() + " " + str(self.getPromedio())

# lista_alumnos=[]
# corte = input("Desea ingresar datos de persona s/n: ")
# while corte != "n":
#     nombre = input("Nombre: ")
#     edad = int(input("Edad: "))
#     dni = input("DNI: ")
#     promedio = input("Promedio: ")
#     un_alumno = Alumno(nombre,edad,dni,promedio)
#     lista_alumnos.append(un_alumno)
#     corte = input("Desea ingresar datos de persona s/n: ")

# contador = 0
# for alumno in lista_alumnos:
#     contador += 1
#     print(str(contador) +") " + alumno.imprimirDatos())