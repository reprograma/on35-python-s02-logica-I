# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#  calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


tamanho_arq_MB = float(input("Qual o tamanho de um arquivo para download em MB? : "))
velocidade_internet = float(input("Qual a velocidade de um link de Internet em Mbps?:  "))

tempo_download_seg = (tamanho_arq_MB / (velocidade_internet/8))
tempo_download_min = tempo_download_seg / 60

print(f" O tempo aproximado de download do arquivo usando este link em minutos é de {tempo_download_min}")