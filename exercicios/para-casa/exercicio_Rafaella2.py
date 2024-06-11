Tamanho_do_arquivo_MB_inserido = input("Insira o tamanho do arquivo para download em MB: ")
Tamanho_do_arquivo_MB = float(Tamanho_do_arquivo_inserido)
Velocidade_do_link_inserido = input("Insira a velocidade do link da internet: ")
Velocidade_do_link = float(Tamanho_do_link_inserido)
Processamento = Tamanho_do_arquivo_MB / Velocidade_do_link

Processamento_por_segundo = 1,25
Segundos_para_Minutos = 60
Resultado_em_minutos = (Processamento_por_segundo * Segundos_para_Minutos)
print(Resultado_em_minutos)



