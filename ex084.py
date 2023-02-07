'''todomundo = list()
dados = list()
pessoas = list()
pessoascad = 0
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
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
    if len(todomundo) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
print(f'O maior peso foi {maior}', end=' ')
for p in todomundo:
    if p[1] == maior:
        print(f'[{p0}]\n')
print(f'O menor peso foi {menor}', end=' ')
for p in todomundo:
    if p[1] == menor:
        print(f'[{p0}]\n')
print(f'Cadastramos {pessoascad} pessoas\n'
      f'CADASTRADOS:\n'
      f'{todomundo}')
'''


temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()
    if resp in 'nN':
        break
print(f'Ao todo temos {len(princ)}')
print(f'O maior peso foi de {mai}Kg peso de', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {men}Kg peso de ',end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end='')
