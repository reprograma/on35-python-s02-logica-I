#Exercício de sala - Aluna Karine Lessa

#Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Olá, mundo!")

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = input("Digite um número: ")
print(f"O número informado foi: {numero} ")

#Faça um Programa que peça dois números e imprima a soma.

numero1 = input("primeiro número é:")
numero2 = input("segundo número é:")
soma = int(numero1) + int(numero2)
print(f"A soma dos números é: {soma}")

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = 8
nota2 = 5.5
nota3 = 9
nota4 = 6.5
print(f"A primeira nota é: {nota1}")
print(f"A segunda nota é: {nota2}")
print(f"A terceira nota é: {nota3}")
print(f"A quarta nota é: {nota4}")

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média bimestral é: {media}")

#Faça um Programa que converta metros para centímetros.

medida_em_metros = float(input("Insira a medida em metros:"))

def conversao(medida_em_metros):
    medida_em_cm = medida_em_metros * 100
    return medida_em_cm 

resultado = conversao(medida_em_metros)
print(f"{medida_em_metros} Metros corresponde a {resultado}cm")