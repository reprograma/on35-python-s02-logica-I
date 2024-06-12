# Exercício de Casa 🏠 Atividade-02 

# Solicita o tamanho do arquivo e a velocidade da internet
tamanho_do_arquivo_em_megabytes = float(input("Tamanho do arquivo (MB): "))
velocidade_da_internet_em_megabits_por_segundo = float(input("Velocidade da internet (Mbps): "))

# Converte a velocidade de megabits por segundo para megabytes por segundo
velocidade_da_internet_em_megabytes_por_segundo = velocidade_da_internet_em_megabits_por_segundo / 8

# Calcula o tempo de download em minutos
tempo_de_download_em_minutos = (tamanho_do_arquivo_em_megabytes / velocidade_da_internet_em_megabytes_por_segundo) / 60

# Exibe o tempo de download
print(f"Tempo aproximado de download: {tempo_de_download_em_minutos:.2f} minutos.")

