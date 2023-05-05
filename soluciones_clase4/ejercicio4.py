class Empleado:

    def __init__(self,nombre,sueldo_base):
        self.__nombre = nombre
        self.__sueldo_base = sueldo_base
    
    def getNombre(self):
        return self.__nombre
    
    def getSueldoBase(self):
        return self.__sueldo_base

    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def setSueldoBase(self,sueldo_base):
        self.__sueldo_base = sueldo_base
    
    def calcularSueldoACobrar(self):
        pass
    
class Jugador(Empleado):

    def __init__(self,nombre,sueldo_base,partidos,goles):
        super().__init__(nombre,sueldo_base)
        self.__partidos = partidos
        self.__goles = goles

    def getPartidos(self):
        return self.__partidos
    
    def getGoles(self):
        return self.__goles
    
    def setPartidos(self,partidos):
        self.__partidos = partidos
    
    def setGoles(self,goles):
        self.__goles = goles
    
    def calcularSueldoACobrar(self):
        sueldo = self.getSueldo()
        promedio_goles = self.getGoles() / self.getPartidos()
        if promedio_goles > 0.5:
            sueldo = suledo * 2
        return sueldo

class Entrenador(Empleado):

    def __init__(self,nombre,sueldo_base,campeonatos):
        super().__init__(nombre,sueldo_base)
        self.__campeonatos = campeonatos
    
    def getCampeonatos(self):
        return self.__campeonatos
    
    def setCampeonatos(self,campeonatos):
        self.__campeonatos = campeonatos
    
    def calcularSueldoACobrar(self):
        sueldo = self.getSueldo()
        campeonatos = self.getCampeonatos()
        if campeonatos >= 1 and campeonatos <= 4:
            sueldo = sueldo + 5000
        elif campeonatos >= 5 and campeonatos <= 10:
            sueldo = sueldo + 30000
        elif campeonatos > 10:
            sueldo = sueldo + 50000
        else:
            pass

        return sueldo