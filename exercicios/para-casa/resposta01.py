vlr_hora=float(input("\nInforme quanto vale a hora trabalhada: "))
num_hora=float(input("Informe a quatidade de horas trabalhadas: "))

calc_salario= lambda vlr_hora,num_hora: vlr_hora*num_hora
soma_salario= calc_salario(vlr_hora,num_hora)

desc_imposto_renda=(soma_salario*11)/100
desc_inss=(soma_salario*8)/100
desc_sindicato=(soma_salario*5)/100

total_desconto= desc_imposto_renda+desc_inss+desc_sindicato
salario_liquido= soma_salario-total_desconto

print(f"\n+Salário Bruto: R$ {soma_salario:.2f}")
print(f"-IR(11%): R$ {desc_imposto_renda:.2f}\n-Inss(8%):R$ {desc_inss:.2f}\n-Sindicato(5%): R$ {desc_sindicato:.2f}")

print(f"=Sálario líquido R$ {salario_liquido:.2f}")