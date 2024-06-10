# 1. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 
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

sal_hora= float(input("Informe seu salário/hora:R$ "))
horas_mes= float(input("Informe horas trabalhadas no mês: "))
salario_mensal = sal_hora*horas_mes
print ('Salário bruto: R$', salario_mensal)

desconto_ir=salario_mensal*0.11
print ('Desconto IR: R$', desconto_ir)

desconto_inss=salario_mensal*0.08
print ('Desconto INSS: R$', desconto_inss)

desconto_sindicato=salario_mensal*0.05
print ('Sindicato: R$', desconto_sindicato)

salario_liquido=salario_mensal-desconto_sindicato-desconto_inss-desconto_ir
print ('Total a receber: R$', salario_liquido)


# 2. Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
# a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def conversao (tamanho): 
    MB= 8*Mb
    return Mb

def conversao (velocidade): 
    Mbps = Mb/60
    return Mbps
    
tamanho= float(input("Informe o tamanho do arquivo em MB: "))
velocidade = float(input("Informe a velocidade em Mbps da Internet: "))
tempo_download= tamanho/velocidade
print ('Tempo para download:', tempo_download)
