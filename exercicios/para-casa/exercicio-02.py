#Exercicio 2 08/06

#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
#velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo_mb = float(input("Inserir o tamanho do arquivo para realização de download em MB: "))
Velocidade_do_link_mbps = float(input("Inserir a velocidade do link da internet em Mbps: "))
conversão = (tamanho_arquivo_mbarquivo_mb/8)

tempo_de_download_segundos = conversão / Velocidade_do_link_mbps

tempo_de_download_minutos = (tempo_de_download_segundos / 60)

print(f"Tempo de download do arquivo é {tempo_de_download_minutos:.2f} minutos")