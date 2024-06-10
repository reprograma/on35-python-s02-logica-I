ganho_por_hora = float(input('informe quanto você ganha por hora trabalhada: '))
horas_trabalhadas = float(input('informe quantas horas você trabalha por mês: '))

salario_bruto = ganho_por_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
tx_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - tx_sindicato

print(f"O seu salário bruto é: R$ {salario_bruto}")
print(f"Você paga R$ {ir} de IR")
print(f"Você paga R$ {inss} de INSS")
print(f"Você paga R$ {tx_sindicato} ao sindicato")
print(f"Seu salário líquido é: {salario_liquido}")