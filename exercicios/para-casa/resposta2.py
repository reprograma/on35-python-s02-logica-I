
tam_arquivo=int(input("Informe o tamnho do aquivo para dowload (em MB): "))
velocidade_internet=int(input("Informe a velocidade da internet (em Mbps): "))

calculo= velocidade_internet/8
resultado=tam_arquivo/calculo

print(f"O tempo aproximado de download do arquivo usando este link é {resultado:.0f}")

