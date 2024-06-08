# 5. Faça um Programa que converta metros para centímetros.

medida_em_metros = float(input('Insira a medida em metros: '))


def conversao(medida_em_metros):
    medida_em_cm = medida_em_metros * 100
    return medida_em_cm


resultado = conversao(medida_em_metros)

print(f'{medida_em_metros} metros corresponde a {resultado}cm')
