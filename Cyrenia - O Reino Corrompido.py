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
#adendos adicionados para que a pessoa utilize no computador e obtenha a melhor experiência possível.
print('PS. Aqui na plataforma Repl eu não consigo passar a experiência exatamente como gostaria para você... \n'
      'isso ocorre devido à algumas funções que por algum motivo a plataforma não executa, por exemplo o sleep,\n'
      'ao executar a função sleep eu conseguiria te passar o texto "epico" gradativamente porém aqui ele salta na sua tela \n'
      'caso queira ter a experiência completa: \n'
      'não se preocupe não há virus no link. É o mesmo código, caso tenha qualquer duvída pode me perguntar no email: claudiocajado@outlook.com.br\n'
      'a proposito meu nome é cláudio tenho 25 anos e sou estudante de programação (ADS - ESTÁCIO) Espero que se divirta jogando o meu joguinho tanto quanto\n'
      'eu me diverti/ estressei fazendo!! BOA JORNADA JOGADOR!\n')
sleep(3)
#Texto inicial para entreter e fisgar o jogador para que ele fique atento ao jogo
textoinicial = 'Em um reino distante chamado Cyrenia, que já havia sido corrompido pela magia de grandes bruxas, feiticeiras e magos, que, depois de ' \
               'obterem o poder absoluto - vindo do livro "MOR`TERR`Á" - se viraram contra todos de suas vilas, realizando... bem... \n' \
               'O rei de Cyrenia, o último sobrevivente de sua raça - os anões, conhecidos por serem leais a todos apesar de reclusos - estava sendo ' \
               'mantido preso por um elfo, Kranowarf, que estava sendo enfeitiçado pelas bruxas. \n' \
               'Depois de tanto tempo sofrendo com a corrupção, o povo de Cyrenia se juntou em cercos para eliminar toda a corrupção de seu reino. ' \
               'Ainda que fracos e inexperientes, havia aqueles que se destacavam. \n' \
               'Os elfos do norte, grandes assassinos furtivos capazes de se camuflar em multidões, usavam adagas e armas de curto alcance para ' \
               'fazer com que seus inimigos desapareçam em segundos. Hoje lutam para salvar o seu líder, Kranowarf \n' \
               'Os grandes vampiros do sul, apesar de traiçoeiros - juntaram-se aos outros, suas grandes habilidades de recuperação de vida, ' \
               'força extrema e suas longas garras o ajudam a eliminar todos a sua frente... só cuidado para não perder o controle! Eles não possuem' \
               'objetivo mas sabem que se o rei continuar onde está e todos os Cyrenianos continuarem sem líder este reino não sobreviverá.\n' \
               'E os magos, antes grandes estudiosos do leste, hoje tentam como podem sobreviver. Eles são os maiores atingidos pela corrupção; ' \
               'sua alma pulsa ao chegar perto dela. Em todo seu âmago, lutam contra e desejam combater e destruir o livro "MOR`TERR`Á".\n'
for str in textoinicial:
    print(str, end='')
    sleep(0.06 * 1)
