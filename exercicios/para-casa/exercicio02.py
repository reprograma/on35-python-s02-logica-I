# 2 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
#  de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo 
# usando este link
#(em minutos).
print("iniciando o calculo do download")

velocidade = float(input("informe a velocidade em mbps da internet: "))
tamanho = float(input("informe o tamanho do arquivo em Mb: "))
conversao = velocidade / 8
tempo_downloadsegundos = tamanho / conversao
tempo_downloadminutos = velocidade/60
print(f"o tempo de dowload é de:{tempo_downloadminutos:.2f}")




