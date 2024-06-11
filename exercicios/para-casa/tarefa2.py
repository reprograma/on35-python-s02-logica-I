tamanho_arquivo_mb = int(input('Informe o tamanho do arquivo (em MB): '))
velocidade_link_mbps = int(
    input('Informe a velocidade do link de Internet (em Mbps): '))


def calcula_tempo_download(tamanho_arquivo_mb, velocidade_link_mbps):
    velocidade_download_mb_s = velocidade_link_mbps * 8
    tempo_download_minutos = tamanho_arquivo_mb / velocidade_download_mb_s
    return tempo_download_minutos


print(f'O tempo aproximado para o download do arquivo é de {
      int(calcula_tempo_download(tamanho_arquivo_mb, velocidade_link_mbps))} minutos.')
