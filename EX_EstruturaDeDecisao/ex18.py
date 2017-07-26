__author__ = 'leohck'

print('>.....----- EX 18 ----.....< ')

"""
Faça um Programa que peça uma data no formato dd/mm/aaaa 
e determine se a mesma é uma data válida.
"""


while True:
   data = str(input('informe uma data no formato dd/mm/aaaa\n><>>: '))
   data = data.split('/')
   if int(data[0]) >= 1 and int(data[0]) <= 31:
       if int(data[1]) >= 1 and int(data[1]) <= 12:
           if len(data[2]) == 4 and int(data[2]) <= 2017:
               print('esta é uma data valida')
               print('/'.join(data))
               break
           else:
               print('informe um ano valido: ')
       else:
           print('informe um mes valido: ')
   else:
       print('informe um dia valido: ')