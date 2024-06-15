#exercicio1

hora_trabalhada = float(input("Insira quantas horas você trabalhou -> "))
salario_por_hora = float(input("Insira quanto vale a sua hora trabalhada -> "))
salario_bruto = hora_trabalhada * salario_por_hora



def salario_liquido(salario_bruto):
    taxas = 0.11 * salario_bruto + 0.08 * salario_bruto + 0.05 * salario_bruto
    salario_liquido = salario_bruto - taxas
    return salario_liquido

salario_liquido_valor = salario_liquido(salario_bruto)


print (f"O salário liquido da pessoa é de R$ {salario_liquido_valor}")


#exercicio2

##Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

MB = float(input("Insira quandos MB tem o arquivo -> "))
Mbps = float(input("Insira quanto tempo em mega por segundo vai levar -> "))

def tempo_aproximado_download_minutos(MB, Mbps):
    tempo_de_download = (MB / Mbps) / 60
    return tempo_de_download

tempo_de_download_do_arquivo = tempo_aproximado_download_minutos(MB, Mbps)

print(f"O tempo de demora para baixar o arqui é de aproximadamente {tempo_de_download_do_arquivo}")