Altura = float(input("Digite a sua altura: "))
Peso = float(input("Digite seu peso: "))

IMC = Peso / (Altura ** 2)

if IMC < 18.5:
    print(f"Magreza")

elif IMC >= 18.5 and IMC < 24.9:
    print(f"Normal")

elif IMC >= 25 and IMC < 29.9:
    print(f"Sobrepeso")

elif IMC >= 30 and IMC < 39.9:
    print(f"Obesidade")

elif IMC >= 40:
    print("Obesidade Grave")
