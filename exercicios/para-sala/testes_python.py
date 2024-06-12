def calcula_media(primeira_nota, segunda_nota):
    media = (primeira_nota + segunda_nota)
    return media

media_joazinho = calcula_media(1, 2)
media_mariazinha = calcula_media (4, 5)

def converter_celcious_para_faremheint(celcius):
    faremheint = (celcius * 9 / 5) + 32
    return faremheint

temperatura_em_faremhaeint = converter_celcious_para_faremheint(100)
print(temperatura_em_faremhaeint)

def junta_nome_e_sobrenome (nome, sobrenome):
    nome_e_sobrenome = nome + " " + sobrenome
    return nome_e_sobrenome

