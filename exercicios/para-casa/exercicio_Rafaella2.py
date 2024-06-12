Tamanho_do_arquivo_MB_inserido = float(input( "Insira o tamanho do arquivo para download em MB: "))
Velocidade_do_link_inserido = float(input("Insira a velocidade do link da internet (Mbps): "))
Conversão = (Tamanho_do_arquivo_MB_inserido/8)

Resultado_em_Mbts = Conversão / Velocidade_do_link_inserido

Resultado_em_minutos = (Resultado_em_Mbts / 60)

print(f"A velocidade aproximada em minutos é de: {Resultado_em_minutos} minutos")

