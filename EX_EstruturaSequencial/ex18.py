"""
Faça um programa que peça o tamanho de um arquivo para download (em MB)
a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
__author__ = 'leohck'

print('>-------------------- EX 18 -------------------<')

tamanho = float(input('Informe o tamanho do arquivo em MB\n><>>: '))
velocidade = float(input('Informe a velocidade da internet em (Mbps)'))

tempo = tamanho/velocidade

print('tempo estimado para download é de : %.2f minutos'%(tempo/60))