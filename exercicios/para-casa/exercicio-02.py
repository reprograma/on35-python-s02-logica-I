# 2. Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

arquivo_mb = float(input('Digite o tamanho do arquivo para download (em MB): '))
velocidade_download = float(input('Digite sua velocidade de internet: '))
conversao = (arquivo_mb/8)

resultado_segundos = conversao / velocidade_download

resultado_minutos = (resultado_segundos / 60)

print(f'O resultado em minutos do download do link é de {resultado_minutos :.2f} minutos')