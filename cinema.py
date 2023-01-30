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
sleep(1)
ano = 2023
filme = 0
while filme <= 0:
    filmename = ''
    sleep(0.2)
    print(f'ESCOLHA SEU FILME ', end=' ')
    filme = int(input('[1] [2] [3] [4]'))
    if filme == 1:
        filmename = 'Pantera Negra'
    if filme == 2:
        filmename = 'Adão Negro'
    if filme == 3:
        sleep(0.3)
        idade = int(input('Insira a sua data de nascimento no formato [AAAA]'))
        idade = ano - idade
        if idade >= 18:
            filmename = 'American Pie'
        else:
            sleep(0.2)
            print(magenta + 'VOCÊ NÃO POSSUI IDADE PARA ASSISTIR A ESTE FILME, A LUCAFILM AGRADECE A PREFERÊNCIA' + reset_color)
            break
    if filme == 4:
        filmename = 'Avatar'
    if filme not in range(1, 5):
        filme = 0
        sleep(0.2)
        print('Por favor insira um valor valido')
    continue
while True:
    if filme == 1:
        sleep(0.3)
        horario = int(input('\nHORARIOS:\n1 - 13:20\n2 - 14:40\n3 - 18:20\n'))
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
        sleep(0.3)
        horario = int(input('\nHORARIOS:\n1 - 12:00\n2 - 16:40\n3 - 23:40\n'))
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
    if filme == 3 and idade >= 18:
        horario = int(input('\nHORARIOS:\n1 - 22:35\n2 - 22:45\n3 - 00:00\n'))
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
        horario = int(input('\nHORARIOS:\n1 - 14:00\n2 - 15:30\n3 - 18:00\n'))
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
valor = 32.20
meia = 16.10
sleep(0.4)
print('INTEIRA R$32.20')
print('MEIA R$16.10')
while True:
    sleep(0.3)
    numeroDeIngressos = int(input('Quantos ingressos deseja [1 - 50]'))
    if numeroDeIngressos not in range(1, 51):
        sleep(0.3)
        print(red + '[ERROR!] O maximo de ingressos por pessoa é de 50 [ERROR!]' + reset_color)
        continue
    sleep(0.3)
    meias = int(input(f'Número de meia? (o número não deve ultrapassar o número de ingressos)'))
    if meias > 50 or meias > numeroDeIngressos:
        sleep(0.3)
        print(red + f'[ERROR!] O maximo de ingressos "meia" é de {numeroDeIngressos} [ERROR!]' + reset_color)
        continue
    inteiras = numeroDeIngressos - meias
    print(inteiras)
    for c in range (inteiras):
        c += 1
        sleep(0.5)
        print(50 * '-')
        sleep(0.5)
        print(green +f'Ingresso: nº{c}\n' 
                f'Filme:   {filmename}',end=' '
                f'Hora:    {hora}\n'
                f'Inteira: R${valor:.2f}\n' + reset_color)
        sleep(0.5)
        print(50 * '-')
        sleep(0.5)
    for c in range(0, meias):
        c += 1
        sleep(0.5)
        print(50 * '-')
        sleep(0.5)
        print(green +f'Ingresso: nº{c}\n' 
                f'Filme:  {filmename}',end=' '
                f'Hora:   {hora}\n'
                f'Meia:   R${meia:.2f}\n' + reset_color)
        sleep(0.5)
        print(50 * '-')
    break
totaldem = meias * meia
totaldeint = inteiras * valor
tt = totaldem + totaldeint
print(magenta + f'Total a pagar R${tt:.2f}' + reset_color)