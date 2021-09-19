numero_da_conta = int(input('Digite o número da sua conta:'))
saldo = float(input('Digite seu saldo:'))
debito = float(input('Digite seu débito:'))
credito = float(input('Digite seu crédito:'))
saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print('SALDO POSITIVO')
else:
    print('SALDO NEGATIVO')