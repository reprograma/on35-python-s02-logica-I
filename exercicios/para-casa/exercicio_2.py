#2. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 
# OBS PARA AGNES RS "SE FOSSE COM METROS/CENTÍMETROS/KM, TERIA APANHADO MENOS KKK"

# https://konnet.com.br/como-calcular-o-tempo-de-download-de-um-arquivo/#:~:text=Tudo%20o%20que%20voc%C3%AA%20precisa,8)%20%3D%20tempo%20em%20segundos.
#calculo: Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) =  tempo em segundos.
#conversão de segundos para minutos = tempo em segundos / 60


tamanho_arquivo_mb = float(input("Qual o tamanho para download em MB? "))
velocidade_internet_mbps = float(input("Qual a velocidade do link de internet em Mbps? "))

conversao_mbps_para_mb = velocidade_internet_mbps / 8  # 1 byte = 8 bits, divide o valor da velocidade_internet_mbps por 8 para converter em megabytes

tempo_download_segundos = tamanho_arquivo_mb / conversao_mbps_para_mb
tempo_download_minutos = tempo_download_segundos / 60  # divisão por 60 para converter o tempo para minutos

print(f"O tempo aproximado de download do arquivo é: {tempo_download_minutos:.2f} minutos")






1