
#criar função

def definir_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

print(definir_media(8, 7))
print(definir_media(10, 9))


def infomracoes_pessoais(nome, idade, cidade, divida, saldo):
    tem_nome_sujo = divida > saldo
    return f"A pessoa {nome}, de {idade} anos, residente de {cidade} tem nome sujo? {tem_nome_sujo}"

print(infomracoes_pessoais("Xainã França", 24, "Recife", 560, 4350))

