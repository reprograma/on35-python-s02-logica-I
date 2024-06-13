
tamanho_arquivo = float(input("Tamanho do arquivo para download (em MB)?: "))
velocidade_link = float(input("Qual a velocidade do link de Internet (em Mbps)?: "))


velocidade_link_MBps = velocidade_link / 8
tempo_download_segundos = tamanho_arquivo / velocidade_link_MBps
tempo_download_minutos = tempo_download_segundos / 60


print(f"\nO tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")