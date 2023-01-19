"""numero = 0
while numero < 16:
    numero += 1
    print(numero)
    if numero == 14:
        break
    """

"""n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))"""

from random import randrange
from time import sleep
par = False
impar = False
vitorias = 0
while True:
    print('\033[35m*=*\033[m'*9)
    v = 1 #variavel controle da verificação do digito
    escolha = input(' escolha par ou impar P/I').upper().strip()[0]
    if escolha in 'P':
        par = True
    elif escolha in 'I':
        impar = True
    else:
        print('\033[31m resposta invalida tente denovo \033[1;35m"voce é idiota" by crau\033[m')
        continue
    computador =randrange(6)
    print(f'computador{computador}')
    while v ==1:
        numero = int(input('digite um numero de 0 a 5'))
        if numero <0 or numero >5:
            print('numero invalido tente outro')
        else:
            v = 0
    soma = numero + computador
    if soma%2 == 0:
        if par == True:
            vitorias += 1
            print('voce escolheu PAR e o computador IMPAR')
            sleep(1)
            print(f'voce jogou{numero} e o computador{computador}. total de {soma} deu PAR')
            print('\033[1;32mvoce venceu\033[m')
            par = False
        else:
            print('voce escolheu IMPAR e o computador PAR')
            sleep(1)
            print(f'voce jogou{numero} e o computador{computador}. total de {soma} deu IMPAR')
            print('\033[1;31m voce perdeu\033[m')
            impar = False
            break
    else:
        if impar == True:
            vitorias += 1
            print('voce escolheu IMPAR e o computador PAR')
            sleep(1)
            print(f'voce jogou{numero} e o computador{computador}. total de {soma} deu IMPAR')
            print('\033[1;32mvoce venceu\033[m')
            impar = False
        else:
            print('voce escolheu IMPAR e o computador PAR')
            sleep(1)
            print(f'voce jogou{numero} e o computador{computador}. total de {soma} deu PAR')
            print('\033[1;31m voce perdeu\033[m')
            par = False
            break
print(f'voce conseguiu uma sequencia de {vitorias} vitorias')