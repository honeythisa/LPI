# Escreva um programa que solicite 10 números ao usuário e, a cada número digitado,
# escreva na tela se este número é positivo ou negativo. Para seu teste informe números
# negativos colocando um sinal de – (menos) antes do número. Por exemplo: -7

i = 0

print('Você pode colocar um sinal de - (menos) antes do número, se quiser, é claro.')

while i <= 10:
    n = int(input('Digite um número:') )
    if n >= 0:
        print('O número digitado é positivo.')
        i = i + 1
    else:
        print('O número digitado é negativo')


print('Fim do programa.')
