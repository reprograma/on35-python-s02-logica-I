salario_hora = float(input("Qual o valor da sua hora trabalhada: "))
horas_mes = float(input("Quantas horas você trabalha no mês: "))
salario_bruto = float(salario_hora) * float(horas_mes)

desc_ir = float(salario_bruto) * 0.11
desc_inss = (float(salario_bruto) - float(desc_ir)) * 0.08
desc_sind = float(salario_bruto) * 0.05
salario_liquido = float(salario_bruto) - float(desc_ir) - float(desc_inss) - float(desc_sind)

print(f"\nSeu salário bruto é {salario_bruto:.2f}\n")
print(f" - Desconto IR (11%): R$ {desc_ir: .2f} reais\n")
print(f" - Desconto INSS (8%): R$ {desc_inss: .2f} reais\n")
print(f" - Desconto Sindicato (5%): R$ {desc_sind: .2f} reais\n")
print(f" = Seu salário líquido é: R$ {salario_liquido: .2f} reais")

