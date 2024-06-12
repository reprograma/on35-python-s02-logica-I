tamanho = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade do link em mbps: "))

tamanho_em_mb = tamanho * 8

download = (tamanho_em_mb / velocidade) / 60

print(f"O tempo aproximado de download do arquivo é de {download:.2f} minutos.")
