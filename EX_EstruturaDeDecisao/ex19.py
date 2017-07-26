__author__ = 'leohck'

print('>.....----- EX 19 ----.....< ')

"""
Faça um Programa que leia um número inteiro menor que 1000 e 
imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. 

Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 

326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
while True:
    n = [0,0,0,0]
    numero = int(input('digite um numero inteiro menor que 1000\n ><>>: '))
    nO = numero
    if numero <1000:
        for i in range(0,len(str(numero))):
            n[i] = numero%10
            numero = int(numero/10)
        if n[0]!= 0 and n[1] != 0 and n[2] != 0:
            print('%i = %i centenas, %i dezenas e %i unidades'%(nO,n[2],n[1],n[0]))
            break
        elif n[0] != 0 and n[1] != 0 and n[2] == 0:
            print('%i =  %i dezenas e %i unidades' % (nO, n[1], n[0]))
            break
        elif n[0]!= 0 and n[1] == 0 and n[2] != 0:
            print('%i = %i centenas e %i unidades'%(nO,n[2],n[0]))
            break
        elif n[0] == 0 and n[1] != 0 and n[2] != 0:
            print('%i = %i centenas e %i dezenas'%(nO,n[2],n[1]))
            break
        elif n[0] != 0:
            print('%i = %i unidades'%(nO,n[0]))
            break
        elif n[1] != 0:
            print('%i = %i dezenas'%(nO,n[1]))
            break
        elif n[2] != 0:
            print('%i = %i centenas'%(nO,n[2]))
            break




