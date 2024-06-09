def media():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota:"))
    nota3 = int(input("Digite a terceira nota:"))
    nota4 = int(input("Digite a quarta nota: "))

    return (nota1 + nota2 + nota3 + nota4) / 4


resultado = media()

print("A média é: ", resultado)
