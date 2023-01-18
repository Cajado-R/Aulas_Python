valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite um número: '))
print(50* '-')
print('SELECIONE\n[1]- SOMAR\n[2]- MULTIPLICAR\n[3]- MAIOR NÚMERO\n[4]- DIGITAR DE NOVO\n[5]- SAIR DO PROGRAMA ')
print(50* '-')
tipo = int(input('Selecione 1 - 5: '))
if tipo == 1:
    print('\033[1:32mO resultado da soma foi {}\033[m'.format(valor1 + valor2))
if tipo == 2:
    print('\033[1:32mO resultado da sua multiplicação foi {}\033[m'.format(valor1 * valor2))
if tipo == 3:
    if valor1 > valor2:
        print('\033[1:32mO maior valor é o primeiro, sendo {}\033[m'.format(valor1))
    if valor2 > valor1:
        print('\033[1:32mO maior valor é o segundo, sendo {}\033[m'.format(valor2))
    if valor2 == valor1 or valor1 == valor2:
        print('\033[1:32mValores iguais\033[m')
while tipo != 5:
        print('SELECIONE\n[1]- SOMAR\n[2]- MULTIPLICAR\n[3]- MAIOR NÚMERO\n[4]- DIGITAR DE NOVO\n[5]- SAIR DO PROGRAMA ')
        tipo = int(input('Selecione 1 - 5: '))
        if tipo == 1:
            print('\033[1:32mO resultado da soma foi {}\033[m'.format(valor1 + valor2))
        if tipo == 2:
            print('\033[1:32mO resultado da sua multiplicação foi {}\033[m'.format(valor1 * valor2))
        if tipo == 3:
            if valor1 > valor2:
                print('\033[1:32mO maior valor é o primeiro, sendo {}\033[m'.format(valor1))
            if valor2 > valor1:
                print('\033[1:32mO maior valor é o segundo, sendo {}\033[m'.format(valor2))
            if valor2 == valor1 or valor1 == valor2:
                print('\033[1:32mValores iguais')
        if tipo == 4:
            valor1 = int(input('\033[1:32mDigite um número: '))
            valor2 = int(input('\033[1:32mDigite um número: '))
if tipo == 5:
    print('\033[1:32mobrigado por usar o meu programa')