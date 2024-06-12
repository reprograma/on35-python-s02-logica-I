#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de 
# um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
#  usando este link (em minutos).

tamanho_do_arquivo_MB_inserido = input('insira o tamanho do arquivo em MB')
tamanho_do_arquivo_MB = float(tamanho_do_arquivo_MB_inserido)
velocidade_internet_inserido = input('insira a valociade da internet em Mbps')

velocidade_internet_mbps = float(velocidade_internet_inserido)
velocidade_internet_mbps_para_MBps = velocidade_internet_mbps * 0.125

tempo_download_segundos = tamanho_do_arquivo_MB / velocidade_internet_mbps_para_MBps
tempo_download_minutos = tempo_download_segundos/60 
print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")