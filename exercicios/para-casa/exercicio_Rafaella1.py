Salario_por_hora = float(input('insira seu salário por hora: '))
Horas_Trabalhadas = float(input('insira a quantidade de horas trabalhadas no mês: '))
Salario = Salario_por_hora * Horas_Trabalhadas
IR = (11 / 100)
INSS = (8 / 100)
Sindicato = (5 / 100)

Desconto_IRRF = Salario * IR
print (f"Desconto de IRRF: {Desconto_IRRF}")

Desconto_INSS = Salario * INSS 
print (f"Desconto de INSS: {Desconto_INSS}")

Desconto_Sindicato = Salario * Sindicato
print (f"Desconto de Sindicato: {Desconto_Sindicato}")

Salario_liquido = Salario-(Desconto_INSS + Desconto_IRRF + Desconto_Sindicato)
print(f"O salário líquido é de: {Salario_liquido}")




