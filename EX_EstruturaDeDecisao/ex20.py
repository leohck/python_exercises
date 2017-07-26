__author__ = 'leohck'

print('>.....----- EX 20 ----.....< ')

"""
Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar:

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
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

