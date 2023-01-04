vdigit = int(input('Digite um número para descobrir se ele é impaer ou par: '))
vdigitt = vdigit % 2
if vdigitt == 0:
    print('Par')
else:
    print('Impar')