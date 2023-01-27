from time import sleep
reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"
print(50*'-')
print(green+ '            Seja Bem vindo ao LucaFilm          ' +reset_color)
print(50*'-')
print(' \nFILMES EM CARTAZ HOJE:\n1 - Pantera Negra \n2 - Adão Negro\n3 - American Pie (+18)\n4 - Avatar')
sleep(1.5)
ano = 2023
filme = 0
while filme <= 0:
    filmename = ''
    print(f'ESCOLHA SEU FILME ', end=' ')
    filme = int(input('[1] [2] [3] [4]'))
    sleep(0.7)
    if filme == 1:
        filme = 1
    if filme == 2:
        filme = 2
    if filme == 3:
        idade = int(input('Insira a sua data de nascimento no formato [AAAA]'))
        idade = ano - idade
        if idade >= 18:
            filme = 3
        else:
            print('VOCÊ NÃO POSSUI A IDADE PARA ASSISTIR A ESTE FILME, A LUCAFILM AGRADECE A PREFERÊNCIA')
            break
    if filme == 4:
        filme = 4
    if filme not in range(1, 4):
        filme = 0
        print('Por favor insira um valor valido')
    continue
while True:
    if filme == 1:
        horario = int(input('\nHORARIOS:\n1 - 13:20\n2 - 14:40\n3 - 18:20\n'))
        sleep(0.7)
        if horario == 1:
            hora = '13:20'
            break
        if horario == 2:
            hora = '14:40'
            break
        if horario == 3:
            hora = '18:20'
            break
        if horario not in range(1, 3):
            print('Escolha um valor valido')
            continue
    if filme == 2:
        horario = int(input('\nHORARIOS:\n1 - 13:20\n2 - 14:40\n3 - 18:20\n'))
        if horario == 1:
            hora = '12:00'
            break
        if horario == 2:
            hora = '16:40'
            break
        if horario == 3:
            hora = '23:40'
            break
        if horario not in range(1, 3):
            print('Escolha um valor valido')
            continue
    if filme == 3:
        horario = int(input('\nHORARIOS:\n1 - 13:20\n2 - 14:40\n3 - 18:20\n'))
        if horario == 1:
            hora = '22:35'
            break
        if horario == 2:
            hora = '22:45'
            break
        if horario == 3:
            hora = '00:00'
            break
        if horario not in range(1, 3):
            print('Escolha um valor valido')
            continue
    if filme == 4:
        horario = int(input('\nHORARIOS:\n1 - 13:20\n2 - 14:40\n3 - 18:20\n'))
        if horario == 1:
            hora = '14:00'
            break
        if horario == 2:
            hora = '15:30'
            break
        if horario == 3:
            hora = '18:00'
            break
        if horario not in range(1, 3):
            print('Escolha um valor valido')
            continue
numeroDeIngressos = 50
while True:
    numeroDeIngressos = int(input('Quantos ingressos deseja [0 - 50]'))
    if numeroDeIngressos not in range(1, 50):
        print(red + '[ERROR!] O maximo de ingressos por pessoa é de 50 [ERROR!]' + reset_color)
        continue
    for count in range (numeroDeIngressos):
        print(f'{filme}       {hora}       {count}')
        
print('bla')
