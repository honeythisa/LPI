inicio = int(input('Que horas começou o jogo?:'))
final = int(input('Que horas terminou o jogo?:'))

if inicio < final:
    duracao = final - inicio
else:
    duracao = (24 - inicio) + final

print ('O jogo durou', duracao,'horas.')

