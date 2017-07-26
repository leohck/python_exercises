"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.

"""

__author__ = 'leohck'

print('-------------------- EX 8 -----------------')

ganha = float(input('Quanto voce ganha por hora? \n ><>>: '))
horas = int(input('Quantas horas voce trabalhou no mes? \n ><>>: '))

salario = ganha * horas

print('O seu salário do mes é de %.2f'%salario)