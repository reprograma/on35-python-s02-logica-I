#Vamos saber quanto será seu salário líquido este mês

horas_trabalhadas = float(input('Quantas horas você trabalhou no mês?'))
salario_por_hora = float(input('Quanta custa sua hora?'))


salario_bruto = (horas_trabalhadas * salario_por_hora)
print('+ Salário Bruto : R$', salario_bruto)

#calcular descontos 11% IR 8% INSS 5% Sindicato 

ir = salario_bruto * 0.11
print('- IR (11%) : R$', ir)

inss = salario_bruto * 0.08
print('- INSS (8%) : R$' , inss)

sindicato = salario_bruto * 0.05
print('- Sindicato (5%) : R$' , sindicato)

salario_liquido = salario_bruto - ir - inss - sindicato
print('=Salário líquido : R$', salario_liquido)
