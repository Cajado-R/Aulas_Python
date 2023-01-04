import random
velcar = random.randint(0, 312) #loat(input('KM carro: '))
if velcar > 80:
    print('Você ultrapassou os 80Km/h, você estava há {}Km/h, a sua multa é de R${:.2f}'.format(velcar, (velcar-80) * 7))
else:
    print('Você estava na velocidade correta parabéns')