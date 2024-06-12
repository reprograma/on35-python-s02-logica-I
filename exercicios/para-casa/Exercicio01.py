valor_por_Hora_trabalhada = float (input("insira o valor por hora trabalhada:"))
quantidade_de_horas_trabalhadas = float (input("insira a quantidade de horas trabalhadas:"))

valor_bruto_mensal =(valor_por_Hora_trabalhada*quantidade_de_horas_trabalhadas)
print (valor_bruto_mensal)

valor_inss = (valor_bruto_mensal*8)/100
print(valor_inss)

valor_sindicato = (valor_bruto_mensal*5)/100
print(valor_sindicato)

valor_ir = (valor_bruto_mensal*11)/100

descontos =(valor_inss+valor_sindicato+valor_ir)
print(descontos)

salario_liquido =(valor_bruto_mensal-descontos)
print (salario_liquido)