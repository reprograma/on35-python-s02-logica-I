salario_bruto = horas_trabalhadas * ganho_por_hora

ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - ir - inss - sindicato
return salario_bruto, ir, inss, sindicato, salario_liquido

ganho_por_hora = float(input("Quanto você ganha por hora? R$"))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario_bruto, ir, inss, sindicato, salario_liquido = calcular_salario(horas_trabalhadas, ganho_por_hora)

print("+ Salário Bruto : R$", salario_bruto)
print("- IR (11%) : R$", ir)
print("- INSS (8%) : R$", inss)
print("- Sindicato (5%) : R$", sindicato)
print("= Salário Liquido : R$", salario_liquido)

