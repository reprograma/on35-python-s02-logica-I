## Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:


valor_hora_trabalhada = float(input("Escreva aqui o valor da sua hora trabalhada, por favor:"))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês "))

salario_bruto = valor_hora_trabalhada * horas_trabalhadas

desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato

print(f"O salário líquido é de R$ {salario_liquido}")


#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)

tamanho_MB = float(input("Tamanho do arquivo para download (em MB)"))
velocidade_mbps = float(input("velocidade (em Mbps)"))

conversao = velocidade_mbps * 8
print(conversao)
tempo_download = conversao / 60
print(tempo_download)

print(f"O tempo aproximado de download do arquivo em minutos é: {tempo_download}")
