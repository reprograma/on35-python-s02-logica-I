# Exercício de Sala 🏫  

## Lógica 1

## Faça um Programa que converta metros para centímetros.

metragem = float(input("informe a metragem: "))

def conversao(metragem):
    medida_em_cm = (metragem) * 100
    return medida_em_cm

resultado = conversao(metragem)

print(f"{float(metragem)} mertros corresponde a {int(resultado)}cm")