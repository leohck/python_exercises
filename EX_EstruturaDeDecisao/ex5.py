__author__ = 'leohck'

print('>.....----- EX 5 ----.....< ')

"""
Faça um programa para a leitura de duas notas parciais de um aluno. 

O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;

A mensagem "Reprovado", se a média for menor do que sete;

A mensagem "Aprovado com Distinção", se a média for igual a dez
"""
def nota(n1,n2):
    media = (n1+n2)/2
    mensagem = ''
    if media >= 7:
        mensagem = 'Aprovado'
    elif media < 7:
        mensagem = 'Reprovado'
    if media == 10:
        mensagem = 'Aprovado com Distincão'

    return mensagem + ' media = %.2f'%media



n1,n2 = float(input('digite sua primeira nota: ')),float(input('digite sua segunda nota: '))
print(nota(n1,n2))

