def metros_para_centimetros():
    metros = float(input("Insira a quantidade em metros: "))
    centimetros = metros * 100
    return centimetros

resultado = metros_para_centimetros()
print("O resultado da conversão é", resultado, "centímetros")
