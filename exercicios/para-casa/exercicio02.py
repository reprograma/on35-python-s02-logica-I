#2. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


tamanho_arquivo = input("Qual o tamanho do seu arquivo em MB? ")
velocidade_internet = input("Qual a velocidade da internet em Mbps? ")

velocidade_internet_mb = float(velocidade_internet) /8

tempo_download = float(tamanho_arquivo) / float(velocidade_internet_mb)

download_minuto = float(tempo_download) / 60

print(f'Tempo aproximado de download : {download_minuto} min')