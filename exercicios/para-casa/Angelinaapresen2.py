arquivo_mb=int(input(" Digite o tamanho do arquivo aqui: "))
velocidade_internete=int(input(" Digite a velocidade da internt: "))

conversao = velocidade_internete * 8
print(conversao)
tempo_donwload = conversao / 60
print(tempo_donwload)

print(f'O Tempo download em minutos é: {tempo_donwload:}')