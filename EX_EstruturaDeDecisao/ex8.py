__author__ = 'leohck'

print('>.....----- EX 8 ----.....< ')

"""
Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
"""
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

produto =[0,0,0]
for i in range(3):
    produto[i] = float(input('Informe o valor do produto %i: '%(i+1)))

if produto[0] == produto[1] and produto[1] == produto[2]:
    print('os tres produtos possuem o mesmo valor!')
else:
    print('Voce deve comprar o produto de RS%.2f pois ele é o mais barato'%Menor(produto))