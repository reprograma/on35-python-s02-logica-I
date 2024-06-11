# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo_download = float(input("Diga o tamanho do arquivo para download em MB:"))

velocidade_link_internet = float(input("Diga  a velocidade do link de internet em Mbps:"))

tempo_do_download_segundos = tamanho_arquivo_download / velocidade_link_internet

tempo_do_download_minutos = tempo_do_download_segundos / 60

print(f"O tempo aproximado de download do arquivo usando este link é de {tempo_do_download_minutos:.2f} minutos.")
