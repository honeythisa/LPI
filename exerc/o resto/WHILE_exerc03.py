# Escreva um programa que receba 2 números do usuário e imprima na tela todos os
# números inteiros do primeiro até o segundo número (inclusive exibindo os números
# escolhidos pelo usuário).

num_1 = int( input('Digite um número:') )
num_2 = int( input('Digite outro número:') )
i = 0

if num_1 > num_2:
    resultado = num_1 - num_2
    while i <= resultado:
        print(num_1 - i)
        i = i + 1
else:
    resultado = num_2 - num_1
    while i <= resultado:
        print(num_1 + i)
        i = i + 1