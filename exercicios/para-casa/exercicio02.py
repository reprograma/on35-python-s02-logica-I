tamanho_arquivo_mb = float (input("digite o tamanho do arquivo para download"))

velocidade_internet_mbps = float(input("digite a velocidade da internet em mbps"))

velocidade_internet_mbps = velocidade_internet_mbps/8

tempo_download_em_segundos = tamanho_arquivo_mb/velocidade_internet_mbps

tempo_download_em_minutos = tempo_download_em_segundos / 60


print (f"tempo de download em minutos e de {tempo_download_em_minutos:.2f}")

