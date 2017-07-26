__author__ = 'leohck'

print('>.....----- EX 15 ----.....< ')

"""
Faça um Programa que peça os 3 lados de um triângulo. 

O programa deverá informar se os valores podem ser um triângulo. 

Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;

Triângulo Equilátero: três lados iguais;

Triângulo Isósceles: quaisquer dois lados iguais;

Triângulo Escaleno: três lados diferentes;
"""
def Triangulo(l1,l2,l3):
    triangulo = ''
    if l1 == l2 and l2 == l3:
        triangulo = 'Equilátero'
    elif l1 == l2 or l2 == l3 or l1 == l3:
        triangulo = 'Isósceles'
    elif l1 != l2 and l2 != l3:
        triangulo = 'Escaleno'
    return triangulo


is_triangulo = False

while True:
    lt1 = int(input('digite o valor do primeiro lado do triangulo: '))
    lt2 = int(input('digite o valor do segundo lado do triangulo: '))
    lt3 = int(input('digite o valor do terceiro lado do triangulo: '))
    if lt1 + lt2 > lt3 or lt1 + lt3 > lt2 or lt2 + lt3 > lt1:
        is_triangulo = True
        if is_triangulo == True:
            triangulo = Triangulo(lt1, lt2, lt3)
            break
        else:
           print('os lados nao criam um triangulo')

print('Triangulo',triangulo)

