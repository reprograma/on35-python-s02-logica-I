# Exercício de Casa 🏠 

## Lógica 2

#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo_mb=int(input(" Digite o tamanho do arquivo aqui: "))
velocidade_internete=int(input(" Digite a velocidade da internt: "))

conversao = velocidade_internete * 8
print(conversao)
tempo_donwload = conversao / 60
print(tempo_donwload)

print(f'O Tempo download em minutos é: {tempo_donwload:}')
