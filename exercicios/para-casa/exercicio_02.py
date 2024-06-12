##2. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print("inciando calculo de download")
arquivo = float(input("Informe o tamanho do arquivo em MB: "))
velocidade = float(input("Informe a velocidade em Mbps da Internet: "))
   
conversao = velocidade/8
velocidade_segundos = arquivo/conversao
tempo_donwload_minutos = velocidade_segundos / 60


print(f"O Tempo download é de: {tempo_donwload_minutos:.2f} minutos")

