#código do RPG (lembrar de rever)

import emoji
from time import sleep
#import random
#import math
#import pygame
reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"


XP = 0
name = ''
sexo = ''

#RAÇAS E CLASSES ATÉ A PARTE DE TRANSFORMAR OS NOMES EM EMOJIS

racas_ou_classes = [' ', 'Elfo', 'Vampiro', 'Mago']
elfos = [' ', ':elf:', ':elf_dark_skin_tone:', ':elf_light_skin_tone:', ':elf_medium-dark_skin_tone:', ':elf_medium_skin_tone:', ':elf_medium-light_skin_tone:']
vampiros = [' ', ':man_vampire:', ':man_vampire_dark_skin_tone:', ':vampire_medium-dark_skin_tone:', ':vampire_medium-light_skin_tone:']
magos = [' ', ':mage:', ':mage_dark_skin_tone:', ':mage_dark_skin_tone:', ':mage_medium-dark_skin_tone:', ':mage_medium-light_skin_tone:', ':mage_medium_skin_tone:']
emojized_elfos = [emoji.emojize(e) for e in elfos]
emojized_vampiros = [emoji.emojize(v) for v in vampiros]
emojized_magos = [emoji.emojize(m) for m in magos]

print('Raças e Classes disponíveis: ', end=' ')
print(*racas_ou_classes, sep=', ')

escolha_de_raca_ou_classe = int(input('Escolha a Raça ou Classe do seu personagem:\n' + green + '1 - Elfos\n' + reset_color + red + '2 - Vampiros\n' + reset_color + blue + '3 - Magos' + reset_color))
sleep(0.05)

#DEPOIS DA ESCOLHA DE RAÇAS TEMOS A ESCOLHA DA SKIN DE PERSONAGEM

while escolha_de_raca_ou_classe < 1 or escolha_de_raca_ou_classe > 3:
    print( red + '[ERROR]' + reset_color + 'Opção inválida, por favor escolha novamente. [1 - Elfos, 2 - Vampiros , ou 3 - Magos]')
    escolha_de_raca_ou_classe = int(input('Escolha a Raça ou Classe do seu personagem:\n' + green + '1 - Elfos\n' + reset_color + red + '2 - Vampiros\n' + reset_color + blue + '3 - Magos' + reset_color))
if escolha_de_raca_ou_classe == 1:
    print('Escolha o seu personagem: [1; 2; 3; 4; ou 5]')
    print(*emojized_elfos, sep=', ')
    estiloelfo = int(input('... '))
    raca = 'ELFO'
    while estiloelfo < 1 or estiloelfo > 6:
        print('Creio que não tenhamos um estilo para o que você deseja, mas mesmo assim, por favor escolha um dos indicados... e não nos assassine')
        estiloelfo = int(input('... ' ))
        raca = 'ELFO'
if escolha_de_raca_ou_classe == 2:
    print('Escolha o seu personagem: [1; 2; 3; ou 4]')
    print(*emojized_vampiros, sep=', ')
    estilovampiro = int(input('... ' ))
    raca = 'VAMPIRO'
    while estilovampiro < 1 or estilovampiro > 4:
        print('Creio que não tenhamos um estilo para o que você deseja, mas mesmo assim, por favor escolha um dos indicados... e por faovr não sugue nosso sangue')
        estilovampiro = int(input('... ' ))
        raca = 'VAMPIRO'
if escolha_de_raca_ou_classe == 3:
    print('Escolha o seu personagem: [1; 2; 3; 4; 5; ou 6]')
    print(*emojized_magos, sep=', ')
    estilomago = int(input('... ' ))
    raca = 'MAGO'
    while estilomago < 1 or estilomago > 4:
        print('Creio que não tenhamos um estilo para o que você deseja, mas mesmo assim, por favor escolha um dos indicados... e por faovr não nos exploda com sua magia')
        estilomago = int(input('... ' ))
        raca = 'MAGO'
#Nome do personagem:

while True:
    name = input('Digite o nome do seu personagem: ')
    print(f'Olá,' + green +  f'{name} ' + reset_color + 'seja bem vindo, se seu nome estiver INCORRETO digite: "INCORRETO", do contrario digite "CORRETO" independente da escolha')
    certoeerrado = input('Aguardando... ').upper().strip()
    if certoeerrado == 'CORRETO':
        break
    if certoeerrado == 'INCORRETO':
        continue
    else:
        print(f'VOCÊ DIGITOU ALGO QUE EU NÃO PREVI POR FAVOR,' + red + f'{raca}', + reset_color + 'VAMOS TENTAR DE NOVO')
#Aqui se inicia o épico!
print(f'{name}, {raca}')