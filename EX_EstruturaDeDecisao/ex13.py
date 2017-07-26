__author__ = 'leohck'

print('>.....----- EX 13 ----.....< ')

"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), 
se digitar outro valor deve aparecer valor inválido.
"""
semana = ['Domingo','Segunda','Terca','Quarta','Quinta','Sexta','Sabado']
dia = int(input('digite um numero de 1 a 7:  '))
while True:
    for i in range(0,7):
        if dia == (i+1):
            print(semana[i])
            break
    else:
        print('inválido')
        dia = int(input('digite um numero de 1 a 7:  '))
        continue
    break

