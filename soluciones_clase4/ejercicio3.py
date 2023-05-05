class OperacionAritmetica:
    def evaluar(self, num1, num2):
        pass

class Suma(OperacionAritmetica):
    def evaluar(self, num1, num2):
        return num1 + num2

class Resta(OperacionAritmetica):
    def evaluar(self, num1, num2):
        return num1 - num2

class Multiplicacion(OperacionAritmetica):
    def evaluar(self, num1, num2):
        return num1 * num2

class Division(OperacionAritmetica):
    def evaluar(self, num1, num2):
        return num1 / num2

n1 = 40.5
n2 = 3
div = Division().evaluar(n1,n2)
suma = Suma().evaluar(n1,n2)
res = Resta().evaluar(n1,n2)
mul = Multiplicacion().evaluar(n1,n2)

print("La suma es: ",suma)
print("La resta es: ",res)
print("La division es: ",div)
print("La multiplicacion es: ",mul)