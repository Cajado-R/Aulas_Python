#Lista de filmes em cartaz a partir daqui
import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"
print(50*'-')
print(red+'            Seja Bem vindo ao LucaFilm          '+reset_color)
print(50*'-')
#filmes a serem printados
filme0 = ' \nFILME:\n0 - Pantera Negra\nHORARIOS:\n1 - 13:20\n2 - 14:40\n3 - 18:20\n'
filme1 = '\nFILME:\n1 - Adão Negro\nHORARIOS:\n1 - 12:00\n2 - 16:00\n3 - 23:40\n'
filme2 = '\nFILME:\n2 - American Pie (+18)\nHORARIOS:\n1 - 22:35\n2 - 22:45\n3 - 00:00\n'
filme3 = '\nFILME:\n3 - Avatar\nHORARIOS:\n1 - 14:00\n2 - 15:30\n3 - 18:00\n'
while True:
    #caso o nome receba uma string ele irá avançar caso não haja irá printar "nome inválido"
    nome = str(input('Seja bem vindo (digite seu nome):'))
    if not (nome.isalpha()):
        print('Seu nome está digitado corretamente? Tente novamnete')
    else:
        break
print(filme0, 50*'-', filme1, 50*'-', filme2, 50*'-', filme3)
#Lista de filmes em cartaz a partir daqui
film = ['Pantera Negra', '13:20', '14:40', '18:20']
film1 = ['Adão Negro', '12:00', '16:00', '23:40']
film2 = ['Adão Negro', '22:35', '22:45', '00:00']
film3 = ['14:00', '15:30', '18:00']

