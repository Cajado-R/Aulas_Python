lista =[]
dicionario={}
while True:
    dicionario['nome']= input('nome: ')
    while True:
        dicionario['sexo']= input('sexo(M/F): ').upper()[0]
        if dicionario['sexo'] in 'MF':
            break
        else:
            print('sexo invalido só M ou F')

    dicionario['idade']= int(input('idade: '))
    lista.append(dicionario.copy())
    dicionario.clear()
    resposta = input('quer continuar?[S/N]').upper().strip()[0]
    if resposta in 'N':
        break


print(f'o grupo tem {len(lista)} pessoas')
total = 0

for n,d in enumerate(lista):
    total += d['idade']
print(f'a media de idade é de {total/len(lista)}')

for d in lista:
    if d['sexo'] in 'mM':
        print(f'As mulheres foram: {d["nome"]}')