__author__ = 'leohck'

print('>.....----- EX 1 ----.....< ')

"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
x,y = float(input('digite um numero: ')),float(input('digite mais um numero: '))
if x > y:
   print(x)
elif y > x:
    print(y)
else:
    print (x,y)