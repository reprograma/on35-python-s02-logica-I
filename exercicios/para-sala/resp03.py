# 3. Faça um Programa que peça dois números e imprima a soma.

def soma(num1, num2):
    soma = num1 + num2
    return soma

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = soma(num1, num2)
print("A soma dos números é:", resultado)
