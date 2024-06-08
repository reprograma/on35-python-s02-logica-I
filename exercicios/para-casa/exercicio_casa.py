# Exercício de Casa 🏠 

## Lógica 1

# 1. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
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
# = Salário Liquido : R$

print("-------- Calculadora de Salário e Descontos --------")

valor = float(input("Qnt ganha por hora: "))
horas = float(input("Qtd de Horas Trabalhadas no Mês: "))

salario_bruto = valor * horas
valor_inss = salario_bruto * 0.08
valor_ir = (salario_bruto - valor_inss) * 0.11  # a base de calculo do IR é o salario bruto - inss
valor_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - valor_inss - valor_ir - valor_sindicato

print(f'+ Salário Bruto : R$ {salario_bruto:.2f}')
print(f'- INSS (8%) : R$ {valor_inss:.2f}')
print(f'- IR (11%) : R$ {valor_ir:.2f}')
print(f'- Sindicato (5%) : R$ {valor_sindicato:.2f}')
print(f'= Salário Líquido : R$ {salario_liquido:.2f}')

# 2. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print(f'------ Conversor - Tempo para Download em Minutos ------')

arquivo_mb = float(input('Tamanho do arquivo para download (em MB): '))
velocidade_mbps = float(input('Velocidade do link de Internet (em Mbps): '))

conversor_mb = velocidade_mbps / 8 #1 MB (Megabyte) tem 8 Mbps (Megabit)

tempo_minutos = (arquivo_mb / conversor_mb) / 60 #1 Minuto tem 60 segundos

print(f'O tempo aproximado de download do arquivo é de {tempo_minutos:.2f} minutos.')