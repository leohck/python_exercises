__author__ = 'leohck'

print('>.....----- EX 12 ----.....< ')

"""

"""

ganha = float(input('Quanto voce ganha por hora? \n ><>>: '))
horas = int(input('Quantas horas voce trabalhou no mes? \n ><>>: '))
salario_bruto = ganha * horas

if salario_bruto > 900 and salario_bruto <= 1500:
   IR = 0.05 * salario_bruto
elif salario_bruto <= 2500:
    IR = 0.10 * salario_bruto
elif salario_bruto > 2500:
    IR = 0.20 * salario_bruto
else:
    IR = 0 * salario_bruto


INSS = 0.10 * salario_bruto
FGTS = 0.11 * salario_bruto
total_descontos = IR+INSS
salario_liquido = salario_bruto - total_descontos
print('Salário Bruto:(%.2f * %i):\nR$ %.2f'%(ganha,horas,salario_bruto))
print('(-) IR (5%%):\nR$ %.2f'%IR)
print('(-) INSS (10%%):\nR$ %.2f'%INSS)
print('    FGTS (11%%):\nR$ %.2f'%FGTS)
print('    Total de descontos:\nR$ %.2f'%total_descontos)
print('    Salário Liquido:\nR$ %.2f'%salario_liquido)