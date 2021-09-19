i = True
while i:
    n1 = float(input("Digite um número: ") )
    op = str(input("Digite o NOME de uma operação simples: ") )
    n2 = float(input("Digite outro número: ") )

    if op == 'adição':
        r = n1 + n2
        print("{} + {} = {}".format(n1, n2, r) )

    elif op == 'subtração':
        r = n1 - n2
        print("{} - {} = {}".format(n1, n2, r) )

    elif op == 'multiplicação':
        r = n1 * n2
        print("{} x {} = {}".format(n1, n2, r) )

    elif op == 'divisão':
        if n2 == 0:
            print("Isso não é permitido.")
        else:
            r = n1 / n2
            print("{} / {} = {}".format(n1, n2, r) )

    elif op == 'divisão' and n2 == '0':
        print("Isso não é permitido.")

    else:
        print("Pani no sistema, alguém me desconfigurou \n"
              "O nome das operações são: adição, subtração, multiplicação e divisão \n"
              "Escreva do jeito certo e tente novamente.")

    cont = input("Quer fazer outra operação?\n"
                 "RESPONDA: sim ou não: ")
    if cont == "não":
        i = False
    elif cont == "sim":
        i = True
    else:
        print("Não soube se você digitou 'sim ou não'.")
        i = False
print("Fim do programa.")