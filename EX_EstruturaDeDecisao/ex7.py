__author__ = 'leohck'

print('>.....----- EX 7 ----.....< ')
"""
Faça um Programa que leia três números e mostre o maior e o menor.
"""
def Maior(n):
    maior = 0
    if n[0] > n[1]:
        if n[0] > n[2]:
            maior = n[0]
        else:
            maior = n[2]
    elif n[1] > n[2]:
        maior = n[1]
    else:
        maior = n[2]
    return maior

def Menor(n):
    menor = 0
    if n[0] < n[1]:
        if n[0] < n[2]:
            menor = n[0]
        else:
            menor = n[2]
    elif n[1] < n[2]:
        menor = n[1]
    else:
        menor = n[2]
    return menor

n=[0,0,0]
for i in range(3):
    n[i] = int(input('digite um numero: '))

if n[0] == n[1] and n[1] == n[2]:
    print('os tres numeros sao iguais')
else:
    print('Maior numero: ',Maior(n))
    print('Menor numero: ',Menor(n))

