for c in range(1, 7):
    peso = float(input('Qual o seu peso'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('MAIOR: {}'.format(maior))
print('MENOR: {}'.format(menor))

