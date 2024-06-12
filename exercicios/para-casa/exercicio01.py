# Exercício de Casa 🏠 

## Lógica 1

#1. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#```
#+ Salário Bruto : R$`
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#```

valor_hora = input("Quanto você ganha por hora: ")
horas_mes = input("Quantas horas você trabalhou esse mês?: ")

salario_bruto = float(valor_hora) * float(horas_mes)

ir = float(salario_bruto) * 0.11
inss = float(salario_bruto) * 0.08
sindicato = float(salario_bruto) * 0.05
salario_liquido = float(salario_bruto) - float(ir) - float(inss) - float(sindicato)

print(f'Salario bruto : R$ {salario_bruto}')
print(f'IR (11%) : R$ {ir}')
print(f'INSS (8%) : R$ {inss}')
print(f'Sindicato (5%) : R$ {sindicato}')
print(f'Salário líquido : R$ {salario_liquido}')