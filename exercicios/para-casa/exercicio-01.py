

valor_em_horas = float(input("quanto voce ganha por hora?: "))

horas_mes = float(input("quantas horas trabalha por mes?: "))

salario_bruto = valor_em_horas * horas_mes


imposto_renda = salario_bruto*0.11
inss = salario_bruto * 0.8
sindicato = salario_bruto * 0.5

salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print(f"\n+ Salário Bruto : R$ {salario_bruto:.2f}")
print(f"- IR (11%) : R$ {imposto_renda:.2f}")
print(f"- INSS (8%) : R$ {inss:.2f}")
print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
print(f"= Salário Líquido : R$ {salario_liquido:.2f}")






