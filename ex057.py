"""sexo = input('Digite seu sexo [M/F]: ').strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().upper() [0]
print('Sexo {} registrado com sucesso'.format(sexo))

sexo = ''
sexx = ''
while sexo == '' or sexo == '':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo == 'M' or sexo == 'F':
        sexx = sexo
    else:
        sexo = ''
print("o seu sexo é {}".format(sexx))