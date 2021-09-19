# Escreva um programa que peça um número ao usuário. Imprima todos os números entre
# o número informado (inclusive ele) e seu quadrado (inclusive ele).

valor = int( input('Digite um número:') )
r1 = (valor ** 2)
i = valor

print('Os números entre o número informado são:')

while i <= r1:
    print(i)
    i = i + 1

print('Fim do programa')


