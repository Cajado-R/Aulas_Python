def fatorial(num, exibir):
    """
    Realiza o cálculo de fatorial e decide se o cálculo será ou não exibido na tela.
    :param num: O número que será inserido pelo usuario
    :param exibir: informa se deseja ou não exibir o clculo do fatorial
    :return: Retorna o resultado do fatorial caso o parametro exibir seja falso
    """
    global NumeroFatorial
    NumeroFatorial = 1
    for c in range(num, 0, -1):
        NumeroFatorial *= c
    resultado = NumeroFatorial
    if exibir == 'S':
        if num == 1:
            print("1 = 1")
        else:
            for b in range(num, 0, -1):
                if b == 1:
                    print("1 = ", end="")
                else:
                    print(f'{b} X ', end=' ')
            print(NumeroFatorial)
    else:
        return resultado
help(fatorial)
Numero = int(input('Qual o número deseja o fatorial? '))
exi = input('Deseja exibir? ').upper().split()[0]
fatorial(num=Numero, exibir=exi)

