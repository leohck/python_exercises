"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
__author__ = 'leohck'

print('>-------------------- EX 12 -------------------<')

altura = float(input('Informe sua altura \n ><>>: '))

peso_ideal = (72.7*altura) - 58

print('O peso ideal de acordo com sua altura é %.2fkg'%peso_ideal)