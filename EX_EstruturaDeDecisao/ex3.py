__author__ = 'leohck'

print('>.....----- EX 3 ----.....< ')

"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

letra = str(input('digite F ou M apenas\n><>>: '))

if letra == 'F' or letra == 'f':
    print('F - Feminino')
elif letra == 'M'or letra == 'm':
    print('M - Masculino')
elif len(letra) != 1:
    print('digite apenas uma letra')
else:
    print('Sexo inválido')