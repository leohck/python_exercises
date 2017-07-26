__author__ = 'leohck'

print('>.....----- EX 6 ----.....< ')

"""
Faça um Programa que leia três números e mostre o maior deles.
"""
n=[0,0,0]
for i in range(3):
    n[i] = int(input('digite um numero: '))

if n[0] == n[1] and n[1] == n[2]:
    print('os tres numeros sao iguais')
elif n[0] > n[1]:
    if n[0]>n[2]:
        print(n[0])
    else:
        print(n[2])
elif n[1]>n[2]:
    print(n[1])
else:
    print(n[2])

