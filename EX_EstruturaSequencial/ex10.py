"""
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.
"""

__author__ = 'leohck'

print('>-------------------- EX 10 -------------------<')

celsius = float(input('digite a temperatura em graus Farenheit\n><>>: '))

farenheit = celsius*1.8 + 32

print('A temperatura %.2fC é = %iF graus'%(celsius,farenheit))