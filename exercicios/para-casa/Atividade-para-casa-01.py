# Exercício de Casa 🏠 Atividade-01 

valor_por_hora = float(input("insira o valor que você ganha por hora: " ))
numero_de_horas_trabalhadas_no_mes = float(input("insira o número de horas trabalhadas no mês: "))
quantidade_de_minutos_trabalhados_no_mes = float(input("insira os minutos trabalhados no mês (além das horas): "))

minutos_em_decimal = round (quantidade_de_minutos_trabalhados_no_mes / 60, 2)

salario_bruto_mes = round ((numero_de_horas_trabalhadas_no_mes + minutos_em_decimal) * valor_por_hora, 2)


#descontos no mês 
# Imposto de Renda 11% 
valor_desconto_imposto_de_renda = round(salario_bruto_mes * 11/100, 2)


#INSS 8% 
valor_desconto_inss = round(salario_bruto_mes*8/100, 2)

#sindicato 5% 
valor_desconto_sindicato = round (salario_bruto_mes*5/100, 2)


#salário líquido no mês
salario_liquido = round(salario_bruto_mes - valor_desconto_imposto_de_renda - valor_desconto_inss - valor_desconto_sindicato, 2)

print("salário_bruto_mês: ", salario_bruto_mes)
print("valor_desconto_imposto_de_renda: ", valor_desconto_imposto_de_renda)
print("valor_desconto_inss: ", valor_desconto_inss)
print("desconto_sindicato: ", valor_desconto_sindicato)
print("salário líquido: ", salario_liquido)
