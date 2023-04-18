"""
Imprime los valores comprendidos entre (num1 + 1) hasta (num2 - 1)
Por ejemplo: si num1 = 5 y num2 = 12
El resultado sería:
6
7
8
9
10
11
"""
def ne(num1, num2):
    if (num1 > num2):
        aux = num1
        num1 = num2
        num2 = aux
    
    for i in range(num1+1, num2):
        print(i)

ne(2,9)