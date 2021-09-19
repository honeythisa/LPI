quant_atual = int(input('Quanto desse produto temos?'))
quant_max = 95
quant_min = 10
quant_media = ((quant_max + quant_min)/2)

if quant_atual >= quant_media:
    print('Não efetuar compra')
else:
    print('Efetuar compra')
