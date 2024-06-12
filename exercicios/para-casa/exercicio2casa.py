arquivo= float(input("Qual o tamanho do arquivo para download (MB)? "))

velocidade= float(input("Qual a velocidade da internet (Mbps)? "))

download_segundos= arquivo / velocidade
download_minutos= download_segundos / 60

print(f"O seu download será feito em aproximadamente {download_minutos: .2f} minutos")

