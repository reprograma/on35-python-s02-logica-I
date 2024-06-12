# Exercício de Casa 🏠 

## Lógica 1

## Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
##quanto pagou ao INSS.
##quanto pagou ao sindicato.
##o salário líquido.
##calcule os descontos e o salário líquido, conforme a tabela abaixo:

##+ Salário Bruto : R$
##- IR (11%) : R$
##- INSS (8%) : R$
##- Sindicato ( 5%) : R$
##= Salário Liquido : R$

print("Iniciando calculo de salário.")

valor_hora_de_trabalho = input("Informe o valor da hora de trabalho: R$ ")
horas_trabalhadas_no_mes = input("Informe o números de horas trabalhadas no mês: ")

salario_bruto = float(valor_hora_de_trabalho)* float(horas_trabalhadas_no_mes)
print(f"Salário bruto é:R${salario_bruto:.2f}")

desconto_ir = salario_bruto * 0.11
print(f"- IR (11%) :R${desconto_ir:.2f}")

desconto_inss = salario_bruto * 0.08
print(f"- INSS (8%) :R${desconto_inss:.2f}")

desconto_sindicato = salario_bruto * 0.05
print(f"- Sindicato (5%):R${desconto_sindicato:.2f}")

salario_liquido = salario_bruto - desconto_inss - desconto_ir - desconto_sindicato
print(f'= Salário Líquido é:R$ {salario_liquido:.2f}')