medida_em_metros = float(input('Insira as medidas em metros: '))
centimetros_em_metros = 100
resultado = (medida_em_metros * centimetros_em_metros)
print(resultado)


#outra forma de criar o código e mais elaborado.

def conversao(medida_em_metros):
    medida_em_centimetros = medida_em_metros * 100
    return medida_em_centimetros

resultado2 = conversao(medida_em_metros)
print(resultado2)

