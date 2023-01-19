#PAR OU IMPAR??
import random
vitoria = 0
while True:
    pcescolhe = random.randrange(11)
    player = int(input('Escolha um número de 0 a 10'))
    if player > 10 or player < 0:
        print('VOCÊ ESCOLHEU UM NÚMERO QUE NÃO FOI PROGRAMADO!! TENTE DE NOVO')
        continue
    parouimpar = str(input('Par ou Impar [P/I]')).strip().upper()[0]
    if parouimpar not in 'PI':
            print('APENAS PAR OU IMPAR...')
            continue
    resultado = player + pcescolhe
    print(f'Você jogou {player} e o PC jogou {pcescolhe}')
    if resultado % 2 == 0 and parouimpar == 'P' or resultado % 2 != 0 and parouimpar == 'I':
        vitoria += 1
        print('Você Venceu!!')
        continue
    else:
        break
print(f'Você perdeu com {vitoria} vitorias.')