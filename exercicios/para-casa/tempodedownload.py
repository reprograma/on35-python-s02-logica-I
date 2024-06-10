#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
#velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado 
#de download do arquivo usando este link (em minutos)

tamanho_arquivo = float(input('informe o tamanho do arquivo para download (em MB): '))
velocidade = float(input('informe a velocidade do link de Internet (em Mbps): '))

tempo_minutos = (tamanho_arquivo * 8) / (velocidade * 60)

print(f"O tempo aproximado de download do arquivo é de {tempo_minutos:.2f} minutos.")