#
# autores: Cristiano e Michel
# data: 30/08/2023

# 1 - ler uma lista de 5 número reais e imprimir a lista na ordem inversa. (dica use o método “reverse()” )

# entrada de dados
lista = []
for i in range(5):
    lista.append(float(input("Digite um número: ")))

# processamento
lista.reverse()

# saída de dados
print(f"Lista na ordem inversa: {lista}")
      