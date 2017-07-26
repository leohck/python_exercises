"""

Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

__author__ = 'leohck'
n = 0
for i in range(1,5):
    n += float(input('digite a %i nota: '%i))

print('media: %.2f'%(n/4))