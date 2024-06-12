# 2. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def calcula_tempo_download():
    tamanho_arquivo_mb = float(input("Insira o tamanho do arquivo para download (em MB): "))
    velocidade_internet_mbps = float(input("Insira a velocidade do link de Internet (em Mbps): "))

    velocidade_internet_mbps = velocidade_internet_mbps / 8 
    tempo_download_segundos = tamanho_arquivo_mb / velocidade_internet_mbps
    tempo_download_minutos = tempo_download_segundos / 60

    print(f"Tempo aproximado de download: {tempo_download_minutos:} minutos")

calcula_tempo_download()





