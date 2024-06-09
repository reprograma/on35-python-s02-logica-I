#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1= float(input('Digite a nota do primeiro bimestre'))
nota2= float(input('Digite a nota do segundo bimestre'))
nota3= float(input('Digite a nota do terceiro bimestre'))
nota4= float(input('Digite a nota do quarto bimestre'))

media= (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média das notas bimestrais é: {media:.2f}')