## Exercicios para casa dia 08/06
## Lógica 1
#Faça um Programa que pergunte quanto você ganha por hora e o 
#número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido,
#conforme a tabela abaixo:
#+ Salário Bruto : R$`
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

print("Cálculo de Salário")
#Valor ganho por hora e quantas horas trabalhadas no mês?
valor_em_horas = float(input("quanto você ganha por hora?: R$ "))
hora_trabalhadas_mês = float(input("valor de horas trabalhadas no mês?: "))

#Cálculo do Salário bruto
salario_bruto = valor_em_horas * hora_trabalhadas_mês

#Cálculo dos descontos
Desconto_ir = salario_bruto * 0.11 
Desconto_inss = salario_bruto * 0.08
Desconto_sindicato = salario_bruto * 0.05

#Cálculo do Salário Líquido
salario_liquido = salario_bruto - Desconto_ir - Desconto_inss - Desconto_sindicato

print(f"\n+ Salário Bruto : R$ {salario_bruto:.2f}")
print(f"- IR (11%) : R$ {Desconto_ir:.2f}")
print(f"- INSS (8%) : R$ {Desconto_inss:.2f}")
print(f"- Sindicato (5%) : R$ {Desconto_sindicato:.2f}")
print(f"= Salário Líquido : R$ {salario_liquido:.2f}")