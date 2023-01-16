maior = 0
nomes = ''
menosde20 = 0
idademedia = 0
for c in range(1, 5):
    nome = str(input('Digite o primeiro nome:'))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo m or f')).upper()
    if c == 1 and sexo == 'M':
        maior = idade
        nomes = nome
    else:
        if idade > maior and sexo == 'M':
            maior = idade
            nomes = nome
    idademedia += idade
    if idade < 20 and sexo == 'F':
        menosde20 += 1
    '''else:
        if idade < menosde20 and sexo == 'F':
            menosde20'''
print('A média de idades dos participantes é de {}'.format(idademedia / 4))
print('O nome do homem com idade maior é {}'.format(nomes))
print('O número de mulehres abaixo dos 20 anos é {}'.format(menosde20))