# Resolução Exercício 2

tamanho_arquivo_MB = float(input("Informe o tamanho do aquivo em MB: "))
velocidade_link_Mbts = float(input("Informe a velocidade do link em Mbps: "))

# 1 MB (Megabyte) tem 8 Mb (Megabit) - converter MB em Mb
tamanho_arquivo_Mb = tamanho_arquivo_MB / 8

resultado_em_Mbts = tamanho_arquivo_Mb / velocidade_link_Mbts

# 1 minuto tem 60 segundos - converter segundos em minutos
tempo_em_minutos = (resultado_em_Mbts / 60)

print(f"O tempo aproximado em que o download do arquivo usando este link dura é de {tempo_em_minutos} minutos")