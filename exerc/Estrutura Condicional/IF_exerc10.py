dias = input('Esse jogo durou mais de 24 horas?:')
inicial = int(input('Que horas começou o jogo?:'))
final = int(input('Que horas terminou o jogo?:'))
duracao = final-inicial

if dias == 'não':
    print('Esse jogo durou',duracao,'horas.')
else:
    print('Esse jogo durou mais que 1 dia.')

