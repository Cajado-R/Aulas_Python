from time import sleep
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', \
        'oito', 'nove', 'dez', 'onze', 'doze', 'treza', 'quatorze', 'quize', \
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número [0 a 20]'))
    if 0 <= numero <= 20:
        continuar = 'N'
        continuar = str(input('Quer continuar? ')).upper().strip()[0]
        if continuar == 'S':
            print(f'Você escolheu o número: {tupla[numero]}')
            continue
        break
    else:
        print('Você digitou um número fora do intervalo')
        sleep(1)
        continue
print(f'Você escolheu o número: {tupla[numero]}')
