#Faça um Programa que converta metros para centímetros.

def metros_para_centimetros(metros):
    """
    Converte um valor em metros para centimetros
    
    Argumento:
     metros: Valor em metros a ser convertido
     
     Retorno:
      Valor em centimetros
     """
    centimetros = metros * 100
    return centimetros

valor_em_metros = float(input("Digite o valor em metros: "))

valor_em_centimetros = metros_para_centimetros(valor_em_metros)

print(f'{valor_em_metros} metros equivalem a {valor_em_centimetros} centimetros')