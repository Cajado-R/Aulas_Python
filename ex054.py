maior = 0
menor = 0
for c in range(7):
    nascimento = int(input('Digite o seu ano de nascimento'))
    if 2023 - nascimento >= 18:
        maior += 1
    else:
        menor += 1
print('{} atingiram a maior idade, e {} ainda não a atingiram.'.format(maior, menor))


