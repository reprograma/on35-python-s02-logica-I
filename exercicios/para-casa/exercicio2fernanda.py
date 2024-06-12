# Exercício de Casa 🏠 

## Lógica 2

#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo_mb=int(input(" Digite o tamanho do arquivo aqui: "))
velocidade_internet=int(input(" Digite a velocidade da internt: "))
link_arquivo=(arquivo_mb * velocidade_internet) / 60 
print(link_arquivo)

print(f'O tempo aproximado de dowload do aquivo em minutos é, {link_arquivo}')


#Tempo de download (em minutos) = Tamanho do arquivo (em MB) / (Velocidade da internet (em Mbps) / 8)
