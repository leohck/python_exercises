"""
Faça um Programa que peça a temperatura em graus Farenheit, transforme e
mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""
__author__ = 'leohck'

print('>-------------------- EX 9 -------------------<')

farenheit = int(input('digite a temperatura em graus Farenheit\n><>>: '))

celsius = (5*(farenheit-32)/9)

print('A temperatura %i F é = %.2f C graus'%(farenheit,celsius))