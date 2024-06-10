valorHora = float(input("Insira quanto você ganha por hora: "))
horasTrabalhadas = float(input("Insira o número de horas trabalhadas: "))

salarioBruto = valorHora * horasTrabalhadas

ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05


salarioLiquido = salarioBruto - ir - inss - sindicato

print("Salário Bruto : R$", salarioBruto)
print("IR (11%) : R$", ir)
print("INSS (8%) : R$", inss)
print("Sindicato (5%) : R$", sindicato)
print("Salário Liquido : R$", salarioLiquido)
