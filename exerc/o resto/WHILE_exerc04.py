# Faça o mesmo programa do exercício anterior, no entanto, desta vez imprima apenas
# os números entre os valores escolhidos, ou seja, os números escolhidos pelo usuário
# não devem ser exibidos.

num_1 = int( input('Digite um número:') )
num_2 = int( input('Digite outro número:') )
i = 0

if num_1 > num_2:
    resultado = num_1 - num_2
    while i < resultado - 1:
        print(num_1 - i - 1)
        i = i + 1
else:
    resultado = num_2 - num_1
    while i < resultado - 1:
        print(num_2 - i - 1)
        i = i + 1