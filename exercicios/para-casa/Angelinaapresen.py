ganha_hora= float(input("digite aqui o valor"))
hora_trabalhada=float(input("digite aqui horas trabalhadas"))
salario_bruto=(ganha_hora * hora_trabalhada)
print(salario_bruto)

desconto_inss= (salario_bruto * 0.08)
print(desconto_inss) 

desconto_ir=(salario_bruto * 0.11)
print(desconto_ir)

desconto_sindicato=(salario_bruto * 0.05)
print(desconto_sindicato) 

salario_liquido=(salario_bruto - desconto_inss - desconto_ir - desconto_sindicato )
print(salario_liquido)  

ganha_hora= float(input("digite aqui o valor"))
hora_trabalhada=int(input("digite aqui horas trabalhadas"))
salario_bruto=(ganha_hora * hora_trabalhada)
print(f"Salário Bruto: R$ {salario_bruto:}")
 
desconto_inss= (salario_bruto * 0.08)
print(f"Desconto INSS (8%): R$ {desconto_inss:}")

desconto_ir=(salario_bruto * 0.11)
print(f"Desconto IR (11%): R$ {desconto_ir:}")

desconto_sindicato=(salario_bruto * 0.05)
print(f"Desconto Sindicato (5%): R$ {desconto_sindicato:}") 

salario_liquido=(salario_bruto - desconto_inss - desconto_ir - desconto_sindicato )
print(f"Salário Líquido: R$ {salario_liquido:}")  

#exercio 1
