#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$`
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
# Salário Liquido : R$

salario_por_hora = float(input("Diga quanto você ganha por hora:"))
numero_horas_trabalhadas =  float(input("Diga quantas horas você trabalha por mês:")) 

salario_bruto = salario_por_hora * numero_horas_trabalhadas

desconto_IR = salario_bruto * 0.11
desconto_INSS = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (desconto_IR + desconto_INSS + desconto_sindicato)

print(f"Salário Bruto : R$ {salario_bruto:.2f}")
print(f"IR (11%) : R$ {desconto_IR:.2f}")
print(f"INSS (8%) : R$ {desconto_INSS:.2f}")
print(f"Sindicato (5%) : R$ {desconto_sindicato:.2f}")
print(f"Salário Líquido : R$ {salario_liquido:.2f}")
