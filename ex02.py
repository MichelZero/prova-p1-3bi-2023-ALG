#
# autores: Cristiano e Michel

# 2 - Em linguagem Python, faça um programa que leia 6 valores e os armazene em uma lista, imprima a 
# lista e mostre o maior elemento e a posição que ele se encontra. (dica use o método index(maior).

# entrada de dados
lista = []
for i in range(6):
    lista.append(float(input("Digite um número: ")))
    
# processamento
maior = max(lista)
posicao = lista.index(maior)

# saída de dados
print(f"Lista: {lista}")
print(f"Maior elemento: {maior}")
print(f"Posição do maior elemento: {posicao}")
