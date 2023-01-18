num = 0
nm = 0
somadetodos = 0
maior = 0
media = 0
menor = 0
continuar = 'S'
while continuar == 'S':
    num = float(input('Digite um número'))
    if maior > num:
       maior = maior
    else:
       if maior < num:
        maior = num
    if menor > num:
        menor = menor
    else:
        if menor < num:
            menor = num
    somadetodos += num
    nm += 1
    continuar = str(input('Deseja continuar [S/N]')).upper()

media = somadetodos / nm

print(maior)
print(menor)
print(media)