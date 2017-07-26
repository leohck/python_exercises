__author__ = 'leohck'

print('>.....----- EX 9 ----.....< ')

"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.

"""

numeros = [0,0,0]
for i in range(3):
    numeros[i] = int(input(u'Informe um número!: '))
numeros = sorted(numeros,reverse=True)
print(numeros)
