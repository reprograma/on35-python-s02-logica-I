# 1. Faça um Programa que pergunte quanto você ganha por hora e o número 
# de horas trabalhadas no mês. Calcule e mostre o total do seu salário 
# no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#  8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salario = float(input ("insira o valor do seu salário: "))
horas_trabalhadas = float (input ("Insira quantas horas trabalhadas no dia: "))
horas_mensais = float(input ("Horas trabalhadas no mês "))

# insira o valor bruto do seu salário
salario_bruto = float(input("Insira o valor bruto do seu salário: "))

#ganho por hora

def float ganho_hora = salario / horas_mensais
float(input(f"O valor de ganho por hora é de: {ganho_hora}"))



# valor descontato por Imposto de renda

IR = salario_bruto * 0,11

# valor descontato por INSS

INSS = salario_bruto * 0,08

# valor descontado para sindicato

sindicato = salario_bruto * 0,05

# salario liquido

salario_liquido = salario_bruto - (IR + INSS + sindicato)

print(f"Salario bruto mensal: R$ {salario_bruto}")
print(f"IR (11%): R$ {IR}")
(f'sindicato (5%): R$ {sindicato} ')
(f'INSS (8%): {INSS}')
(f' Salário líquido mensal: {salario_liquido}')



