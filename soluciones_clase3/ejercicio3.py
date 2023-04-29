class Temperatura():

    def __init__(self):
        self.__temperatura = 0
    
    def getTemperatura(self):
        return self.__temperatura
    
    def setTemperatura(self, temp):
        self.__temperatura = temp

    def calcularCelsius(self,temp_fh):
        en_fh = (temp_fh - 32.0) * (5/9)
        self.setTemperatura(en_fh)
        return en_fh

    def calcularFarenheit(self,temp_cels):
        en_cels = (temp_cels * (9/5)) + 32.0
        self.setTemperatura(en_cels)
        return en_cels

###aplicacion#####
celsius = float(input("ingrese temperatura en celsius: "))
farenheit = float(input("ingrese temperatura en farenheit: "))
temp = Temperatura()
print("La temperatura en farenheit es: ",temp.calcularFarenheit(celsius))
print("La temperatura en celsius es: ",temp.calcularCelsius(farenheit))