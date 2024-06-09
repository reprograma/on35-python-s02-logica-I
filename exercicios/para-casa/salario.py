# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda,
#  8% para o INSS e 
# 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# ```
# + Salário Bruto : R$`
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário

# (Ctrl+ K + C )  (Ctrl + K+ U)

# salario minimo 2024 :1412,00

salario_hora = int(input("Qual o seu salário por hora?: "))
qtde_hrs_dia = int(input("Quantas horas você trabalha por dia: "))

salario_bruto = (salario_hora * qtde_hrs_dia) * 30
ir_imposto_renda = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - ir_imposto_renda - inss - sindicato

print(f" + Salário Bruto : R$ {salario_bruto}")
print(f" - IR (11%) : R$ {ir_imposto_renda}")
print(f" - INSS (8%) : R$ {inss}")
print(f" - Sindicato ( 5%) : R$ {sindicato}")
print(f" = Salário Liquido :R$ {salario_liquido}")

