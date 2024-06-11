salario_por_hora = float(input("Informe o valor do seu salário por hora: "))
horas_trabalhadas = int(
    input("Informe a quantidade de horas trabalhadas no mês: "))


def calcula_salario(salario_por_hora, horas_trabalhadas):
    salario_bruto = salario_por_hora * horas_trabalhadas
    desc_ir = salario_bruto * 0.11
    desc_inss = salario_bruto * 0.08
    desc_sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - desc_ir - desc_inss - desc_sindicato

    print(f'+ Salário Bruto: R$ {salario_bruto:.2f}')
    print(f'- IR (11%): R$ {desc_ir:.2f}')
    print(f'- INSS (8%): R$ {desc_inss:.2f}')
    print(f'- Sindicato (5%): R$ {desc_sindicato:.2f}')
    print(f'= Salário Líquido: R$ {salario_liquido:.2f}')


calcula_salario(salario_por_hora, horas_trabalhadas)
