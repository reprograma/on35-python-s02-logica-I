def cal_temp_down(arq_down , vel_link_mbps):
    temp_arq_mbps = arq_down * 8
    temp_seg = temp_arq_mbps / vel_link_mbps
    temp_min = temp_seg / 60
    return temp_min

arq_down = float(input("Qual o tamanho do arquivo para download (MB): "))
vel_link_mbps = float(input("Qual a velocidade da sua internet (Mbps): "))

temp_down_min = cal_temp_down(arq_down, vel_link_mbps)

print(f"O tempo de download será de {temp_down_min: .2f} minutos.")