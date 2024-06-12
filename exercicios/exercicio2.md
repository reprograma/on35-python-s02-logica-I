tamanho_arquivo = float(input("Tamanho do arquivo para download (MB): "))
velocidade_internet = float(input("Velocidade do link de Internet (Mbps): "))

tempo_download_minutos = (tamanho_arquivo * 8 / velocidade_internet) / 60

print("Tempo aproximado de download:", round(tempo_download_minutos, 2), "minutos")

