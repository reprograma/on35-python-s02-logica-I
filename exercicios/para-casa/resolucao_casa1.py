ganho_por_hora = float(input("Informe seu ganho por hora no mês: "))
numero_horas_trabalhadas = float(input("Informe quantas horas foram trabalhadas no mês: "))

salario_bruto = ganho_por_hora * numero_horas_trabalhadas
print(f"O seu salário bruto é R$ {salario_bruto} nesse mês")

ir = salario_bruto * 0.11
print(f"Foi descontado R$ {ir} de Imposto de Renda")

inss = salario_bruto * 0.08
print(f"Foi descontado R$ {inss} de INSS")

sindicato = salario_bruto * 0.05
print(f"Foi descontado R$ {sindicato} para o sindicato")

salario_liquido = salario_bruto - (ir + inss + sindicato)
print(f"O seu salário líquido é R$ {salario_liquido} nesse mês")