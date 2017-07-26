"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
"""
__author__ = 'leohck'

print('>-------------------- EX 11 -------------------<')

def a(n1,n2):
    return ((n1*2)*(n2/2))

def b(n1,n2):
    return ((n1*3)+n2)

def c(n1):
    return n1 ** 3

int1 = int(input('Digite um numero inteiro: '))
int2 = int(input('Digite outro numero inteiro: '))
real = float(input('Digite um numero real: '))

print('o produto do dobro do primeiro com metade do segundo:\n %i'%a(int1,int2))
print('a soma do triplo do primeiro com o terceiro:\n %.2f'%b(int1,real))
print('o terceiro elevado ao cubo: \n %i'%c(real))