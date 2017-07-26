"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
__author__ = 'leohck'

print('>-------------------- EX 16 -------------------<')

metros = int(input('Informe o tamanho em metros quadrados da area a ser pintada\n><>>: '))

litros_nescessarios = metros // 3
preco_lata = 80.00

if litros_nescessarios <= 18:
    quantidade = 1
    preco_total = preco_lata
else:
    for i in range(36,360,18):
        if litros_nescessarios <= i:
            quantidade = i/18
            preco_total = preco_lata*quantidade
            break
        else:
            continue

print('Latas nescessarias = %i latas\n'
      'Preco total = R$ %.2f'%(quantidade,preco_total))
print(litros_nescessarios)