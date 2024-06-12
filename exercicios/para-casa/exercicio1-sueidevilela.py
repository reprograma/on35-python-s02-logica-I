ganho = float(input("Digite o quanto você ganha por hora: "))
horas = float(input("Digite o número de horas trabalhadas neste mês: "))

salario = ganho * horas

ir = 0.11 * salario
inss = 0.08 * salario
sindicato = 0.05 * salario

salarioliquido = salario - ir - inss - sindicato

print(f"Salário Bruto: R${salario:.2f}")
print(f"Imposto de Renda: R${ir:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"Sindicato: R${sindicato:.2f}")
print(f"Salário Líquido: R${salarioliquido:.2f}")