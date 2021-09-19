# o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que:
# - Se quantidade <= 5 o desconto será de 2%
# - Se quantidade > 5 e quantidade <=10 o desconto será de 3%
# - Se quantidade > 10 o desconto será de 5%
print('====================DESCRIÇÃO DE UM PRODUTO====================')
nome_do_prod = input('Qual o nome do produto?: ')
quant_adquirida = int(input('Qual foi a quantidade adquirida?: ') )
preco_unit = float(input('Qual é o preço unitário desse produto?: R$ ') )

total = preco_unit * quant_adquirida
valor_a_pg = total - 0.02
valor_a_pg2 = total - 0.03
valor_a_pg3 = total - 0.05

if (quant_adquirida <=5):
    print('O desconto será de 2%')
    print('Total a pagar pelo {} : R$ {}'.format(nome_do_prod, valor_a_pg) ) # 2% do total

if (quant_adquirida >5) and (quant_adquirida <=10):
    print('O desconto será de 3%')
    print('Total a pagar pelo {} : R$ {}'.format(nome_do_prod, valor_a_pg2) ) # 3% do total

if (quant_adquirida >10):
    print('O desconto será de 5%')
    print('Total a pagar pelo {} : R$ {}'.format(nome_do_prod, valor_a_pg3 ) )
