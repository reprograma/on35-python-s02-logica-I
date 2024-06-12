# Faça um Programa que converta metros para centímetros.

medidas_metros = float(input("Por gentileza, digite um número em metros: "))

def conversao (medidas_metros):
    medida_centimetros = medidas_metros * 100
    return medida_centimetros

resultado = conversao(medidas_metros)

print(f"{medidas_metros} metros é igual a {resultado} centímetros.")