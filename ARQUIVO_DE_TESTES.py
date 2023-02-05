import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 300
altura = 300
x = 0
y = 0
t = 10
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura)) # criar uma tela no tamanho da tupla largura e altura
pygame.display.set_caption('joguinho') #nome na janela

while True: #while de eventos principal
    relogio.tick(20)
    tela.fill((13,20,27))#coloca uma tela na frente neste caso preta
    for event in pygame.event.get(): #checar se houve algum evento
        if event.type == QUIT: #se o evento for o quit fechar a janela e o jogo
            pygame.quit() #comando pra fechar
            exit()
    #quadrado                R   G  B     X    Y   L   A
    pygame.draw.rect(tela, (255, 0, 0), (200, 300, 40, 50)) #primeira tupla as cores RGB 255 =vermelho, segunda 200 é o x 300 é o y, 40 largura e 50 altura
    # circulo                 R   G   B     X    Y   RAIO
    pygame.draw.circle(tela, (0, 255, 0), (300, 260), 40) #(300, 260) posição em x e y do meio do circulo, 40 é o raio
    # linha                  R  G  B     X  Y    X   Y  espessura
    pygame.draw.line(tela, (150,0,255),(600,0),(300,altura),5)#primeira tupla é a um ponto e a segunda outro ponto pra linha

    pygame.draw.circle(tela,(150,0,255),(x, y), t)
    x+= 1
    y+= 1
    t+= 1
    if x >= largura:
        x = 0
        y = 0
    if t >= 120:
        t = 10
    pygame.display.update()