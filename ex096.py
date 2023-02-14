def area(l, a):
    area = l * a
    print('Controle de Terrenos')
    print('-'*100)
    print(f'A área do terreno com Largura de: {l}m e comprimento de {a}m é de {area:.2f}m')



largura = float(input('LARGURA: \n'))
comprimento = float(input('COMPRIMENTO: \n'))
area(l = largura, a = comprimento)