def metros_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

metros = float(input("Insira a medida em metros: "))

centimetros = metros_para_centimetros(metros)

print(f"{metros} metros equivalem a {centimetros} centímetros.")