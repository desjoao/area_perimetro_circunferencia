#Lista 5 - Exercício 3

import math
def area (x):
    A = math.pi*x**2
    return A
def perimetro (x):
    P = math.pi*2*x
    return P

raio = float(input('Insira o valor do raio de uma circunferência em cm: '))
print (f'O valor do perímetro da circunferência é {perimetro(raio):.2f}cm e o de sua área é {area(raio):.2f}cm²')
