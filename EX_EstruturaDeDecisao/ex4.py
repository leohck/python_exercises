__author__ = 'leohck'

print('>.....----- EX 4 ----.....< ')

"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
vogal = 'aeiou'
consoante = 'qwrtyiopsdfghjklzxcvbnm'

letra = str(input('digite uma letra\n><>>: '))

if len(letra) != 1:
    print('digite apenas uma letra')
elif letra in vogal:
    print(letra,'vogal')
elif letra in consoante:
    print(letra,'consoante')
else:
    print('isso nao é uma letra!')