numin = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[1] Converter Binário
[2] Converter Octal
[3] Converter Hexadecimal''')
opção = int(input('Opção: '))
if opção == 1:
    print('Binário {}'.format(bin(numin)[2:]))
elif opção == 2:
    print('Octal {}'.format(oct(numin)[2:]))
elif opção == 3:
    print('Hexadecimal {}'.format(hex(numin)[2:]))
else:
    print('ERRO')