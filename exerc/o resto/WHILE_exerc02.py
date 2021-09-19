# Faça o mesmo que o exercício anterior, no entanto, não aceite valores menores que 1
# ou maiores que 10, ou seja, só aceite tabuadas de 1 a 10. Caso o usuário informe um
# valor. Incorreto, exiba uma mensagem informando-o que um valor entre 1 e 10 deve ser
# informado.

valor = int( input('Digite um número para ver sua tabuada:') )

i = 1
while i <= 10:
    if valor <= 10 and valor >= 1:
        print('{} x {} = {}'. format(valor, i, valor*i))
        i = i + 1
    else:
        valor = int(input('Deve ser informado somente números de 1 a 10.'
                          '\n Digite novamente:'))

print('Fim do programa')


