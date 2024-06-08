#2. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

MB = float(input ("Insira o tamanho do arquivo em MB: "))

#conversão megabyte para megabit:
mb = MB * 8

mbps = float(input ("Insira a velocidade de link com a internet em Mbps: "))

#tempo de download em segundos:
seconds = mb / mbps

#tempo em minutos
minutes = seconds / 60

print (f"O tempo estimado de download com este link de internet é {minutes}minutos")