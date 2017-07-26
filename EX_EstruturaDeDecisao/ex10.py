__author__ = 'leohck'

print('>.....----- EX 10 ----.....< ')

"""
Faça um Programa que pergunte em que turno você estuda.
peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
conforme o caso.
"""

turno = str(input('informe o periodo em que voce estuda\n M - matutino ou V - Vespertino ou N - Noturno\n><>>: ')).lower()

while True:
 if turno == 'm' or turno == 'matutino':
     print('Bom Dia!')
     break
 elif turno == 'v' or turno == 'vespertino':
     print('Boa Tarde!')
     break
 elif turno == 'n' or turno == 'noturno':
     print('Boa Noite!')
     break
 else:
     print('Valor Inválido!')
     turno = str(input('informe o periodo em que voce estuda\n M - matutino ou V - Vespertino ou N - Noturno\n><>>: ')).lower()
