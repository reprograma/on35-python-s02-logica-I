# Exercício de Casa 🏠 

# Lógica 1

# 1. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$`
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

def calcula_salario ():
    valor_hora = float(input("Insira o valor que você ganha por hora: "))
    horas_trabalhadas = float(input("Insira o número de horas trabalhadas por mês: "))

    salario_total = valor_hora * horas_trabalhadas

    desconto_ir = salario_total * 0.11  
    desconto_inss = salario_total * 0.08  
    desconto_sindicato = salario_total * 0.05 

    salario_liquido = salario_total - desconto_ir - desconto_inss - desconto_sindicato

    print(f"Salário Bruto: R$ {salario_total:.2f}")
    print(f"Desconto IR (11%): R$ {desconto_ir:.2f}")
    print(f"Desconto INSS (8%): R$ {desconto_inss:.2f}")
    print(f"Desconto Sindicato (5%): R$ {desconto_sindicato:.2f}")
    print(f"Salário Líquido Total: R$ {salario_liquido:.2f}")


calcula_salario()

