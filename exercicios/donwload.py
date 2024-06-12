#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps)

arquivo_mb=int(input('Digite o tamanho do arquivo aqui: '))
velocidade_mbps=int(input('Digite a velocidade da internet: '))

link_arquivo=(arquivo_mb*velocidade_mbps/8) /60

print(f'O tempo aproximado de dowload do aquivo em minutos é, {link_arquivo}')
