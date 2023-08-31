#
# autores: Cristiano e Michel

# 3 - Em linguagem Python, faça um programa que leia um conjunto de 10 números inteiros, 
# armazenando-o em uma lista (L1), calcular o quadrado dos elementos dessa lista, 
# armazenando o resultado em oura lista (L2), imprimir todas as listas.

# entrada de dados
lista = []
for i in range(10):
    lista.append(int(input("Digite um número: ")))
    
# processamento
lista2 = []
for i in range(10):
    lista2.append(lista[i]**2)
    
# saída de dados
print(f"Lista: {lista}")
print(f"Lista2: {lista2}")
