numero = list()
maior = 0
menor = 0
for c in range(0, 5):
    numero.append(int(input(f'Número na posição {c}')))
    if c == 0:
        maior = menor = numero[c]
    else:
        if numero[c] > maior:
            maior = numero[c]
        if numero[c] < menor:
            menor = numero[c]
print(f'o maior valor digitado foi {maior} nas posições: ',end=' ')
for posicao, valor in enumerate(numero):
    if valor == maior:
         print(f'{posicao}', end='...')
print(f'\nE o menor valor digitado foi {menor} nas posições', end=' ')
for posicao, valor in enumerate(numero):
    if valor == menor:
        print(f'{posicao}', end='...')