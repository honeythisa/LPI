# Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou
# não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito:
# - Ter no mínimo 65 anos de idade.
# - Ter trabalhado no mínimo 30 anos.
# - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
# Com base nas informações acima, faça um programa que leia: o ano de seu nascimento
# e o ano de seu ingresso na empresa. O programa deverá escrever a idade e o tempo de
# trabalho do empregado e informar se ele pode ou não requerer a aposentadoria.
# Utilize apenas UM if e um else para todas as condições, não utilizar mais de um if ou
# algum elif.
x = '='
print('{}VERIFICAÇÃO{}'.format(x*30, x*30) )
nasc = int(input("Qual ano você nasceu?: ") )
trab = int(input("Qual ano você ingressou na empresa?: ") )

idade = 2020 - nasc
tempo = 2020 - trab

if ((idade >=65 and tempo >=30) or (idade >=60 and tempo >=25)): print('Você poderá receber a aposentadoria!')

else: print('Você não poderá receber a aposentadoria')