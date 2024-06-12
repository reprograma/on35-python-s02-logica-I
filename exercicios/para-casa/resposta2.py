arquivo_mb = float(input("Qual o tamanho do arquivo em MB: "))
velocidade = float(input("Qual a velocidade da internet em Mbps: "))
tempo = arquivo_mb/velocidade
minuto = tempo / 60

print(f'O tempo para realizar o download aproximadamente sera: %.2f minutos'%minuto)