"""
Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 (h = altura)
Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
"""
__author__ = 'leohck'

print('>-------------------- EX 13 -------------------<')

altura = float(input('Informe a sua altura: '))
sexo = str(input('Informe seu sexo: M/F\n><>>: '))
peso = float(input('Informe seu peso em kg: '))

while True:
 if sexo == 'm' or sexo == 'M':
    peso_ideal = (72.7*altura) - 58
    break
 elif sexo == 'f' or sexo == 'F':
    peso_ideal = (62.1*altura) - 44.7
    break
 else:
    sexo = str(input('Informe seu sexo: apenas ( M / F ) são permitidos \n><>>: '))
    continue

print('O peso ideal de acordo com sua altura é %.2fkg'%peso_ideal)

if peso > peso_ideal:
    print('Voce esta acima do peso ideal para a sua altura!')
elif peso < peso_ideal:
    print('Voce esta abaixo do peso ideal para a sua altura!')
else:
    print('Voce esta no peso ideal')