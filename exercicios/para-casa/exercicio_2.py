#2. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 
# OBS PARA AGNES RS "SE FOSSE COM METROS/CENTÍMETROS/KM, TERIA APANHADO MENOS KKK"



tamanho_arquivo_mb = float(input("Qual o tamanho para download em MB? "))
velocidade_internet_mbps = float(input("Qual a velocidade do link de internet em Mbps? "))

velocidade_internet_mbps = velocidade_internet_mbps / 8  # 1 byte = 8 bits

tempo_download_segundos = tamanho_arquivo_mb / velocidade_internet_mbps
tempo_download_minutos = tempo_download_segundos / 60  # divisão por 60 para converter o tempo para segundos

print(f"O tempo aproximado de download do arquivo é: {tempo_download_minutos:.2f} minutos")






1