arquivo_em_mby = float(input("insira arquivo aqui: "))
velocidade_mpbs = float(input("insira o link aqui: "))

arquivo_em_bi = arquivo_em_mby * 8

velocidade_media = ((arquivo_em_bi * 0.0167) / (velocidade_mpbs))

print(f"A velocidade média do download é de {velocidade_media} por minuto")
