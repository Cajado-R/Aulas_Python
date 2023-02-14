povo = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('M ou F')
    pessoa['idade'] = int(input('Idade: '))
    povo.append(pessoa.copy())
    while True:
        cont = str(input('Quer continuar? [S/N]')).upper()[0]
        if cont in 'SN':
            break
        print('S ou N')
    if cont == 'N':
        break
print(f'Ao todo temos: {len(povo)} pessoas cadastradas')
media = soma / len(povo)
print('As mulheres cadastradas foram: ', end='')
for p in povo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('Acima da média: ',end='')
for p in povo:
    if p['idade'] >= media:
        print(f'A pessoa acima da média é: {p["nome"]}')
print()