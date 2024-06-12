valor_horas = input("Insira o valor que voce ganha por hora: ")
quantidade_horas = input("Insira a quantidade de horas que trabalha por mes: ")

salario = float(valor_horas) * float(quantidade_horas)
ir = (11/100 * float(salario))
inss = (8/100 * float(salario))
sindicato = (5/100 * float(salario))
desconto = ir + inss + sindicato
salario_liquido = salario - desconto

print(f'O valor do salario: R$ {salario}')
print(f'- IR (11%): R$ {ir}')
print(f'- INSS (8%): R$ {inss}')
print(f'- Sindicato (5%): R$ {sindicato}')
print(f'= Salario Liquido: R$ {salario_liquido}')