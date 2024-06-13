hora_trabalhada = float(input("Insira quantas horas você trabalhou -> "))
salario_por_hora = float(input("Insira quanto vale a sua hora trabalhada -> "))

salario_bruto = hora_trabalhada * salario_por_hora

def salario_liquido(taxas):
    salario_liquido = salario_bruto - [(11/100) * salario_bruto] + [(8/100) * salario_bruto] + [(5/100) * salario_bruto]
    return salario_liquido

print(salario_liquido())