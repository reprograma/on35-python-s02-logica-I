arquivo_mb=int(input('Digite o tamanho do arquivo aqui: '))
velocidade_mbps=int(input('Digite a velocidade da internet: '))

link_arquivo=(arquivo_mb*velocidade_mbps/8) /60

print(f'O tempo aproximado de dowload do aquivo em minutos é, {link_arquivo}')