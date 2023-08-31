#
# autores: Cristiano e Michel

# 4 - Escreva um programa que solicite ao usuário que digite uma 
# sequência de números, armazene em uma lista e calcule a média.

# entrada de dados com while
lista = []
while True:
    numero = input("Digite um número ou 'sair' para sair: ")
    if numero == 'sair':
        break
    else:
        lista.append(int(numero))
        
# calculo da média
soma = 0
for numero in lista:
    soma += numero

media = soma / len(lista)
# outra forma de calcular a média usando a função sum
# media = sum(lista) / len(lista)

# saída de dados
print("A média dos números digitados é: ", media)
