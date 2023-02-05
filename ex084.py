todomundo = list()
dados = list()
pessoas = list()
pessoascad = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    todomundo.append(dados[:])
    dados.clear()
    pessoascad += 1
    continuar = input('Deseja continuar? [S/N]').upper().strip()
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
    else:
        print('Apenas sim ou não')
        continue
for p in todomundo:
    if p[1] >= 100:
        pessoas.append(p[0])
        print(f'os mais leves foram {pessoas}')
        pessoas.clear()
    elif p[1] <= 65:
        pessoas.append(p[0])
        print(f'Os mais pesados foram {pessoas}')
print(f'Você cadastrou: {todomundo}')
print(f'Cadastramos {pessoascad} pessoas')
