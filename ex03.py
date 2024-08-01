produtos = {}


for i in range(2):
    print(f"Cadastro do produto {i+1}:")
    codigo = input("Código: ")
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    
    
    produtos[codigo] = {"nome": nome, "quantidade": quantidade, "preco": preco}


print("\nProdutos cadastrados:")
for codigo, produto in produtos.items():
    print(f"Código: {codigo}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")


valor_total = 0
for produto in produtos.values():
    valor_total += produto["quantidade"] * produto["preco"]

print(f"\nValor total das compras: R$ {valor_total:.2f}")