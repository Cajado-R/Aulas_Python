'''nome = input('Nome do jogador: ')

numpartidas = int(input('Número de partidas: '))

dados = []

total = 0

dicionario = {}
print('-' * 50)

for i in range(numpartidas):
    saldo = int(input(f'Na partida {i+1} {nome} fez: '))

    dados.append(saldo)
    total += saldo

dicionario['total'] = total
dicionario['nome'] = nome
dicionario['partidas'] = numpartidas
dicionario['gols'] = dados

print(f'**'*50)

for i, tudo in dicionario.items():
    print(f'O campo {i} tem {tudo}')
print('-=' * 50)
print(f'O jogador {nome} jogou {numpartidas} partidas')

for i, gol in enumerate(dados):
    print(f'Na partida {i+1} ele fez {gol} gols')
print(f'Ele fez um total de {dicionario["total"]} de gols na temporada')
'''

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome: \n'))
numpartidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? \n'))
for c in range(numpartidas):
    partidas.append(int(input(f'Quantos gols na partida {c + 1} fez? \n')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('*' * 25)
print(jogador)
print('-' * 25)
for i, all in jogador.items():
    print(f' O campo {i} tem o valor {all}')
print('*' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f' Na partida {i + 1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')