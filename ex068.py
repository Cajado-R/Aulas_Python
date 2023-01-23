#PAR OU IMPAR??
import random
vitoria = 0
while True:
    #escolhas do pc de 0 a 10 (range 11 para incluir o 10)
    pcescolhe = random.randrange(11)
    player = int(input('Escolha um número de 0 a 10'))
    if player > 10 or player < 0:
        #escolhas apenas entre 0 e 10
        print('VOCÊ ESCOLHEU UM NÚMERO QUE NÃO FOI PROGRAMADO!! TENTE DE NOVO')
        continue
    parouimpar = str(input('Par ou Impar [P/I]')).strip().upper()[0]
    #caso a pessoa escolha algo diferente de Par ou Impar imprima apenas par ou impar e retorne para cima
    if parouimpar not in 'PI':
            print('APENAS PAR OU IMPAR...')
            continue
        #calculo do valor escolhido pelo player e o do pc
    resultado = player + pcescolhe
    #Print de escolha de ambos
    print(f'Você jogou {player} e o PC jogou {pcescolhe}')
    #condição de vitória
    if resultado % 2 == 0 and parouimpar == 'P' or resultado % 2 != 0 and parouimpar == 'I':
        #adicione mais uma vitória condicional
        vitoria += 1
        print('Você Venceu!!')
        #retorne para cima (while)
        continue
    else:
        break
print(f'Você perdeu com {vitoria} vitorias.')