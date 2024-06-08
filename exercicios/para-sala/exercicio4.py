# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("----- Digite suas notas Bimestrais para saber sua Média -----")
b1 = input("Digite a nota do Primeiro Bimestre: ")
b2 = input("Digite a nota do Segundo Bimestre: ")
b3 = input("Digite a nota do Terceiro Bimestre: ")
b4 = input("Digite a nota do Quarto Bimestre: ")

media = (int(b1) + int(b2) + int(b3) + int(b4)) / 4

print(f"Sua média é: {media}")