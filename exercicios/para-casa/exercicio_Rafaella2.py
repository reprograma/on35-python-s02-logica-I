Tamanho_do_arquivo_MB_inserido = input("Insira o tamanho do arquivo para download em MB: ")
Tamanho_do_arquivo_MB = float(Tamanho_do_arquivo_MB_inserido)
Velocidade_do_link_inserido = input("Insira a velocidade do link da internet: ")
Velocidade_do_link = float(Velocidade_do_link_inserido)
Tamanho_arquivo_segundos = Velocidade_do_link * 8
print(Tamanho_arquivo_segundos)
Segundos_para_Minutos = 60
Resultado_em_minutos = (Tamanho_arquivo_segundos / Segundos_para_Minutos)
print(Resultado_em_minutos)




