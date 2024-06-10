tamanhoArquivo = float(input("Insira o tamanho do arquivo: "))
velocidadeMbps = float(input("Insira a velocidade: "))

velocidadeMbps = velocidadeMbps/8

tempoSegundos = tamanhoArquivo / velocidadeMbps

tempoMinutos = tempoSegundos / 60

print("O tempo de download é de", tempoMinutos, "minutos")
