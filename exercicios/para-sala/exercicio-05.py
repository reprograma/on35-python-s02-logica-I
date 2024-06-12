##Faça um Programa que converta metros para centímetros.

def converte_metros_centimetros ():
    metros = float(input("Digite a medida em metros: "))
    centimetros = metros * 100
    print(f"{metros:.0f} metro(s) equivale a {centimetros:.0f} cm" )

converte_metros_centimetros()
