#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
value = float(input ("Insira o valor da sua hora de trabalho: "))
time = float(input ("Insira quantas horas você trabalha por mês: "))

#Calcule e mostre o total do seu salário no referido mês, abaixo primeiro sem os descontos:
gross = value * time

#são descontados 11% para o Imposto de Renda
ir = gross * 0.11

#8% para o INSS
inss = gross * 0.08

#5% para o sindicato
union = gross * 0.05

#salário liquido
net = gross - (ir + inss + union)

print (f"+ Salário Bruto mensal : R${gross}")
print (f"- IR (11%) : R${ir}")
print (f"- INSS (8%) : R${inss}")
print (f"- Sindicato ( 5%) : R${union}")
print (f"= Salário Liquido : R${net}")