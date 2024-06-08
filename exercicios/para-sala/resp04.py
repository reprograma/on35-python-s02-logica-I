# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def calculo_media(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = calculo_media(n1, n2, n3, n4)
print(f"A média das notas é {media}")
