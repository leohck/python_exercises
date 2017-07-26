__author__ = 'leohck'

print('>.....----- EX 11 ----.....< ')

"""
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%
 Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario = float(input('Informe seu salario: '))

if salario <= 280:
   reajuste = (0.20*salario)
   perc = '20%'
elif salario <= 700:
    reajuste = (0.15*salario)
    perc = '15%'
elif salario <= 1500:
    reajuste = (0.10*salario)
    perc = '10%'
else:
    reajuste = (0.05*salario)
    perc = '5%'

novo_salario = reajuste + salario

print('salário antes do reajuste = R$ %.2f'%salario)
print('percentual de aumento aplicado = %s'%perc)
print('valor de aumento = R$ %.2f'%reajuste)
print('sálario, após o aumento = R$ %.2f'%novo_salario)