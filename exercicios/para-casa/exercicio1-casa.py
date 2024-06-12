
salario_hora= float (input("Quanto você ganha por hora? "))
hora_mes= float (input("Quantas horas você trabalha por mês? "))
salario_total= salario_hora * hora_mes

porcentagem_IR= 11
imposto_renda = (porcentagem_IR  / 100 ) * salario_total

porcentagem_INSS= 8
inss = (porcentagem_INSS / 100) * salario_total

porcentagem_sindicato= 5
sindicato = (porcentagem_sindicato / 100) * salario_total

salario_liquido= salario_total - inss - sindicato - imposto_renda

print(f"Salário bruto: R$ {salario_total}")
print(f"Descontado imposto de renda: R$ {imposto_renda}")
print(f"Pago ao INSS: R$ {inss}")
print(f"Pago ao Sindicato: R$ {sindicato}")
print(f"Salário líquido: R$ {salario_liquido}")

