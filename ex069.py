pessoas18 = homem = mulher = 0
continuar = ''
while continuar == '' or continuar == 'S':
    user = str(input('SEXO: [M/F]')).strip().upper()[0]
    if user in 'MF':
        age = int(input('Digite sua idade: '))
    else:
        continue
    if age >= 18:
        pessoas18 += 1
    if age < 20 and user == 'F':
        mulher += 1
    if user == 'M':
        homem += 1
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar not in 'SN':
        continuar = ''
        print('Você digitou algo errado, vamos voltar.')
        continue
    if continuar == 'S':
        continue
    continue
print(f'O total de pessoas com +18 é {pessoas18}')
print(f'Temos um total de {homem} homens cadastrados')
print(f'Temos um total de {mulher} mulheres com menos de 20 anos')
