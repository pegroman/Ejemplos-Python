class Fecha():

    def __init__(self, dia,mes,anio):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
    
    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes

    def getAnio(self):
        return self.__anio

    def setDia(self,dia):
        self.__dia = dia

    def setMes(self,mes):
        self.__mes = mes
    
    def setAnio(self,anio):
        self.__anio = anio
    
    def __str__(self):
        cadena = str(self.getDia) + "/" + str(self.getMes())+ "/" + str(self.getAnio())

class OperacionesFecha():
    def __init__(self,f1,f2):
        self.__fecha1 = f1
        self.__fecha2 = f2
    
    def diferenciaDias(self):
        fe1 = (fecha1.getAnio()*365) + (fecha1.getMes()*30) + fecha1.getDia() 
        fe2 = (fecha2.getAnio()*365) + (fecha2.getMes()*30) + fecha2.getDia() 
        return fe2 - fe1

###aplicacion####
fecha1 = Fecha(30,4,2021)
fecha2 = Fecha(25,6,2022)
resta = OperacionesFecha(fecha1,fecha2)
print(resta.diferenciaDias())

