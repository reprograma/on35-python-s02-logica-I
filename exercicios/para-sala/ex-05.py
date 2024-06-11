#Faça um Programa que converta metros para centímetros.
medida_metros=float(input("Insira a medida em metros: "))

def conversao (medida_metros):
    medida_cm=medida_metros*100
    return medida_cm

resultado=conversao(medida_metros)

print (f'({medida_metros} metros corresponde a {resultado} centimetros')
