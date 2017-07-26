__author__ = 'leohck'

print('>.....----- EX 16 ----.....< ')
from math import sqrt
"""
Faça um programa que calcule as raízes de uma equação do segundo grau, 
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e 
fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, 
a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, 
sendo encerrado;

Se o delta calculado for negativo, a equação não possui raizes reais. 
Informe ao usuário e encerre o programa;

Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

print('Calculo de raiz da EQUACAO DO SEGUNDO GRAU\n><>>: ax2 + bx + c')

while True:
    a = int(input('informe o valor de a: '))
    if a == 0:
        print('nao e uma equacao do segundo grau')
        break
    else:
       b = int(input('informe o valor de b: '))
       c = int(input('informe o valor de c: '))

    delta = (b**2) - (4*a*c)

    if delta < 0:
        print('a equacao nao possui raizes reais.')
        break
    elif delta == 0:
        print('a equacao possui 2 raizes iguais')
        x1 = -b/(2*a)
        x2 = x1
        print('raiz 1 = %i\nraiz 2 = %i' % (x1,x2))
        break
    elif delta > 0:
        print('a equacao possui 2 raizes diferentes')
        x1 = -b + sqrt(delta)/(2*a)
        x2 = -b - sqrt(delta)/(2*a)
        print('raiz 1 = %i\nraiz 2 = %i' % (x1, x2))
        break
