# Resolução Exercício 2

tamanho_arquivo = float(input("Informe o tamanho do aquivo em MB: "))
velocidade_link = float(input("Informe a velocidade do link em Mbps: "))

tempo_download = (tamanho_arquivo * 8) / (velocidade_link)
print(f"O tempo aproximado em que o download do arquivo usando este link dura é de {tempo_download} minutos")