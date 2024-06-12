# 1. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu 
# salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
#
# + Salário Bruto : R$`
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato (5%) : R$
# = Salário Liquido : R$ 

salario_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantidade de horas trabalhadas por mês? "))

salario_bruto = salario_hora * horas_trabalhadas
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
total_descontos = desconto_inss + desconto_ir + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print(f"\nSeu salário bruto é R$ {salario_bruto:.2f} reais.")
print(f"Desconto de imposto de Renda R$ {desconto_ir:.2f} reais.")
print(f"Desconto de INSS R$ {desconto_inss:.2f} reais.")
print(f"Desconto de contribuição sindical R$ {desconto_sindicato:.2f} reais.")
print(f"\nSeu salário líquido é R$ {salario_liquido:.2f} reais.")

