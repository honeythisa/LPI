# Escreva um programa que imprima a TABUADA na tela. Peça que o usuário informe qual
# tabuada deseja visualizar
tabuada = int( input('Qual tabuada você deseja visualizar?:') )
i = 1
while i <= 10:
    print('{} x {} = {}'.format(tabuada, i, tabuada*i))
    i = i + 1

print('Fim do programa.')