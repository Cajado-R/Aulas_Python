num = 0
nm = 0
somadetodos = 0
maior = 0
media = 0
menor = 0
continuar = 'S'
while continuar == 'S':
    num = float(input('Digite um número'))
    somadetodos += num
    nm += 1
    if nm == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    continuar = str(input('Deseja continuar [S/N]')).upper()

media = somadetodos / nm

print(maior)
print(menor)
print(media)

