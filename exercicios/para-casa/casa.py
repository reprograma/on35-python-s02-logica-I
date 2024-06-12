## Lógica 1

#1. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
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


salario_por_hora = input("Quanto você ganha por hora? ")
numero_de_horas = input("Insira o número de horas trabalhadas ")

total_salario = (float(salario_por_hora) * float(numero_de_horas))

desconto_ir = total_salario * 0.11
desconto_inss = total_salario * 0.08
desconto_sindicato = total_salario * 0.05

salario = total_salario - desconto_ir - desconto_inss - desconto_sindicato

print(f'Total do seu Salário é {total_salario}')
print(f'Desconto do IR: {desconto_ir}')
print (f'Desconto do INSS: {desconto_inss}')
print(f'Desconto do sindicato: {desconto_sindicato}')
print(f'Salário liquido: {salario}')



#2. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


tamanho_arquivo = float (input("Qual o tamanho do arquivo para download em MB: "))
velocidade_internet = float(input("Qual é a velocidade de um link de Internet em Mbps: "))

tempo_minutos = tamanho_arquivo / velocidade_internet * 60

print(f'tempo aproximado de download do arquivo usando este link : {tempo_minutos} em minutos')
20