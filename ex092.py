import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = int(date.strftime("%Y"))
while True:
    dados = dict()
    dados['nome'] = str(input('Nome: '))
    dado = int(input('Ano Nascimento: '))
    d3 = year - dado
    dados['idade'] = d3
    if dados['idade'] < 18:
        print('Menor de idade')
        break
    dados['CTPS'] = int(input('CTPS Nº: '))
    if dados['CTPS'] == 0:
        break
    else:
        dados['contratacao'] = int(input('Ano de contratação: '))
        dados['salario'] = float(input('Salário: '))
        dados['aposentadoria'] = dados['contratacao'] - dado + 35
        break
print(dados)
print(f'Nome: {dados["nome"]}\n'
      f'Idade: {dados["idade"]}\n'
      f'CTPS Nº: {dados["CTPS"]}\n'
      f'Contratado em: {dados["contratacao"]}\n'
      f'Salário: {dados["salario"]}\n'
      f'Irá se aposentar com {dados["aposentadoria"]} anos')

for c,k in dados.items():
    print(f'{c} tem o valor {k}')