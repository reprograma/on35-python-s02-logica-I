ganhos_por_hora = float(input("insira ganhos aqui:"))
numero_de_horas = float(input("insira horas aqui:"))

salario_bruto = (ganhos_por_hora) * (numero_de_horas)
print(f"O salario bruto mensal é de {salario_bruto} reais")

ir = (salario_bruto * 11) / 100
print(f"O valor de desconto referente ao IR é de {ir} reais")

inss = (salario_bruto * 8) / 100
print(f"O valor de desconto referente ao INSS é de {inss} reais")

sindicato = (salario_bruto * 5) / 100
print(f"O valor de desconto referente ao INSS é de {sindicato} reais")

salario_liquido = (salario_bruto) - (ir) - (inss) - (sindicato)
print(f"O salário líquido mensal é de {salario_liquido} reais")
