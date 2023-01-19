produtomaisbarato = preco = total = maisde1000 = produtos= 0
continuar = ''
while continuar == '' or continuar == 'S':
    nomeproduto = str(input('Produto: '))
    preco = float(input('Preço: '))
    if preco >= 1000:
        maisde1000 += 1
    produtos +=1
    if produtos == 1:
        produtomaisbarato = preco
    else:
        if preco < produtomaisbarato:
            produtomaisbarato = preco
    total += preco
    continuar = str(input('Continuar? [S/N]')).upper()
    if continuar not in 'SN':
        print('Você digitou algo errado, vamos tentar novamente.')
        continue
    if continuar == 'S':
        continue
    if continuar == 'N':
        print(f'O total foi R${total}')
        print(f'Você comprou {maisde1000} produtos que custam mais de R$1.000,00')
        produtomaisbarato = nomeproduto
        print('O produto mais barato foi {}'.format(produtomaisbarato))

