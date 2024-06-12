#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$`
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

valor_por_hora_inserido = input('Insira seu valor ganho por hora')
valor_por_hora = float(valor_por_hora_inserido)
horas_trabalhadas_inserida = input('Insira as horas trabalhadas')
horas_trabalhadas = float (horas_trabalhadas_inserida)
salario_bruto = (valor_por_hora * horas_trabalhadas) * 22
ir = float(11/100) * salario_bruto 
inss = float(8/100) * salario_bruto
sindicato = float(5/100) * salario_bruto
salario_liquido = (salario_bruto - ir - inss - sindicato)
total =[
    'Seu salário bruto é igual: ' + str(salario_bruto),
    'desconto de INSS é igual: ' + str(inss),
    'desconto de IR é igual: ' + str(ir),
    'desconto sindical é igual: ' + str(sindicato),
    'seu salário líquido é igual: ' + str(salario_liquido)]