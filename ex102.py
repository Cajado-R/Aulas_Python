def fatorial(num, exibir):
    global NumeroFatorial
    NumeroFatorial = 1
    for c in range(num, 0, -1):
        NumeroFatorial *= c
    resultado = NumeroFatorial
    if exibir == 'S':
        for b in range(Numero, 0, -1):
            print(f'{Numero} X {b}', end='')
        return NumeroFatorial
    else:
        return resultado


Numero = int(input('Qual o número deseja o fatorial? '))
exi = input('Deseja exibir? ').upper()
print(fatorial(num=Numero, exibir=exi))
