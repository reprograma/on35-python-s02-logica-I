# def latido():
#     print('auau')

# latido()


# def calcula_media(nota1,nota2):
#     media = (nota1+ nota2) /2
#     return media

# print(calcula_media(10,12))
# print(calcula_media(5,7))



# def gera_apresentacao(nome,idade,onde_mora):
#     apresentacao = f"nome completo: {nome}, idade completa: {idade},endereço: {onde_mora}"
#     return apresentacao


# print(gera_apresentacao("marcela",36,"campinas"))

def retorna_informacoes_pessoais(nome,idade,genero,cidade_natal,cpf,saldo,dividas):
    tem_nome_sujo= dividas > saldo
    return f"A pessoa {nome}, de idade {idade}, genero {genero}, natural de {cidade_natal},de cpf {cpf},tem o nome sujo: {tem_nome_sujo}"

print(retorna_informacoes_pessoais("marcela", 36, "mulher", "Campinas", 1234567890, 10000, 2000))
    