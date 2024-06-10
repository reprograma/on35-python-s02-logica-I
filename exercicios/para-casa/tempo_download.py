#Vamos calcular quanto tempo levará para o seu arquivo fazer o download completo

tamanho_arquivo = float(input('Qual o tamanho do arquivo que você fará o download? (MB)'))

velocidade = float(input('Qual a velocidade? (Mbps)'))

tempo_de_download = velocidade / tamanho_arquivo
print('O tempo de download é aproximadamente ', (tempo_de_download*60) , ' minutos')

