__author__ = 'leohck'

print('>.....----- EX 14 ----.....< ')

"""

Faça um programa que lê as duas notas parciais obtidas por um aluno ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

 Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
"""
n1,n2 = float(input('digite a primeira nota: ')),float(input('digite a segunda nota: '))
media = (n1+n2)/2


conceito = 'APROVADO'

if media <= 10 and media >= 9:
    print('Media = %.2f\nConceito = A'%media)
elif media >= 7.5 and media < 9:
    print('Media = %.2f\nConceito = B' % media)
elif media >= 6 and media < 7.5:
    print('Media = %.2f\nConceito = C' % media)
elif media >= 4 and media < 6:
    print('Media = %.2f\nConceito = D' % media)
    conceito = 'REPROVADO'
elif media >= 0 and media < 4:
    print('Media = %.2f\nConceito = E' % media)
    conceito = 'REPROVADO'

print(conceito)