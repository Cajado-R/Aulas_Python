def fatorial(num, exibir):
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

Numero = int(input('Qual o número deseja o fatorial? '))
exi = input('Deseja exibir? ').upper().split()[0]
fatorial(num=Numero, exibir=exi)
