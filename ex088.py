import random
while True:
    jogos = int(input('Qauntos jogos você quer que eu sorteie? '))
    matriz = []
    for n in range(jogos):
        palpite = []
        for num in range (1, 7):
            inteiros = random.randint(0, 61)
            palpite.append(inteiros)
        matriz.append(palpite)
        print(f'O jogo {n+1} é: {palpite}')
    break
