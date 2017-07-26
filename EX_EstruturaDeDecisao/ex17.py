__author__ = 'leohck'

print('>.....----- EX 17 ----.....< ')

"""
Faça um Programa que peça um número correspondente a um determinado ano 
em seguida informe se este ano é ou não bissexto.
"""
ano = int(input('informe um ano para saber se ele é bissexto\n><>>: '))

is_bissexto = False
if ano % 4 == 0 and ano % 100 != 0:
    is_bissexto = True
elif ano % 400 == 0:
    is_bissexto = True
else:
    is_bissexto = False

if is_bissexto == True:
    print('o ano: %i é um ano bissexto'%ano)
else:
    print('o ano: %i nao é bissexto'%ano)

