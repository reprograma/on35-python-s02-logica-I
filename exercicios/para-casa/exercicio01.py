## Lógica 1

#1. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

#+ Salário Bruto : R$`
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

valor_horas = float(input("valor_da_hora_trabalhada: R$"))
horas_trabalhadas = float(input("numero_de_horas_trabalhadas: "))  
                   
salariobruto = valor_horas * horas_trabalhadas
print(f"salario bruto e:R$ {salariobruto:.2f}")
desconto_IR = salariobruto * 0.11
print(f"Imposto de renda 11%: R$ {desconto_IR:.2f}") 
desconto_inss = salariobruto * 0.08
print(f"desconto de Inss 8 %: R$ {desconto_inss:.2f}") 
desconto_sindicato = salariobruto * 0.05
print(f"desconto do sindicato 5%: R$ {desconto_sindicato:.2f}")
salario_liquido = salariobruto - desconto_IR - desconto_inss - desconto_sindicato
print(f"salario liquido é: R${salario_liquido}") 

                      