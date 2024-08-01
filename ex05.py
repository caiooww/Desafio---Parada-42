def calcular_area(lado1, lado2):
    return lado1 * lado2

print("Você deseja calcular a área de um quadrado ou retângulo?")
print("1 - Quadrado")
print("2 - Retângulo")
escolha = int(input("Digite a opção: "))

if escolha == 1:
    lado = float(input("Digite o lado do quadrado: "))
    area = calcular_area(lado, lado)
    print(f"A área do quadrado é {area:.2f} unidades quadradas.")
elif escolha == 2:
    lado1 = float(input("Digite o comprimento do retângulo: "))
    lado2 = float(input("Digite a largura do retângulo: "))
    area = calcular_area(lado1, lado2)
    print(f"A área do retângulo é {area:.2f} unidades quadradas.")
else:
    print("Opção inválida!")