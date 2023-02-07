import pygame

class Cachorros:
    def __init__(self, nome, cor_de_pelo, idade, tamanho):
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
        self.nome = nome
    def latir(self):
        print('au au')
    def correr(self):
        print(f'{self.nome} está correndo')

cachorro_1 = Cachorros('Toby', 'Preto', 5, 'Enorme')
print(cachorro_1.nome)
print(cachorro_1.correr())