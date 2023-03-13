def ficha(nome, gols):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if not gols.isnumeric():
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'

nome = input('Nome do Jogador\n').strip()
gols = input('Nº de gols\n').strip()

print(ficha(nome, gols))
