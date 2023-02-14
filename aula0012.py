pessoas = {
    'nome':'Cláudio',
    'sexo':'M',
    'idade':22
}
print(f' O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['Peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {
    'uf': 'Rio de Janeiro', 'sigla': 'RJ'
}
estado2 = {
    'uf': 'Bahia', 'sigla': 'BA'
}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])

brasil.clear()
estado1.clear()
estado2.clear()

estado = dict()
brasil = list()
for c in range(0, 2):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
    estado.clear()
for e in brasil:
    for k, v in e.items():
        print(f'O {k} é {v}')