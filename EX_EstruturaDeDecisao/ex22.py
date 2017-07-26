__author__ = 'leohck'

print('>.....----- EX 22 ----.....< ')


print('><>>:LEOHCK ITM:<<><')

print('valore disponivel para saque:\n de R$10 a R$600')
print('notas disponiveis = 1,5,10,20,50,100')

while True:
    v = [0,0,0]
    valor = int(input('informe o valor desejado para o saque\n ><>>: '))
    vO = valor
    if valor >= 10 and valor <= 600:
        for i in range(0,len(str(valor))):
            v[i] = valor % 10
            valor = int(valor/10)
            
    else:
        print('valor indisponivel ')