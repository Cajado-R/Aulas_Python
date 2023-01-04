import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
print(50*'-')
print('                       ')
print(50*'-')
while True:
    try:
        nome = input('Digite o seu nome: ' )
        nome1 = (nome.isalpha())
        if not nome1:
            raise ValueError('Por favor use apenas letras')
        break
    except ValueError as error:
        print(error)
while True:
    try:
        anodenascimento = int(input('Digite o ano de seu nascimento, por favor: '))
        idade = date.year - anodenascimento
        if not 0 <= idade <= 122:
            raise ValueError('Idade invalida!')
        break
    except ValueError as error:
        print(error)
print('FILMES EM CARTAZ\n1 - Pantera Negra\n2 - Adao Negro\n3 - Avatar')
filme = str(input('Digite o número do Filme: ' ))
if filme == '1':
 while True:
    try:
        hora = int(input('Selecione um horario p/ Pantera Negra\n1 - {}\n2 - {}\n3 - {}\n'.format('14:20', '15:35', '17:40')))
        if not 0 <= hora <= 3:
            raise ValueError('Horario fora do intervalo permitido')
        break
    except ValueError as error:
       print(error)
while True:
    try:
        ingresso = int(input('Selecione o número de ingressos '))
        if ingresso == 0 or ingresso > 50:
            raise ValueError('Valor fora do intervalo permitido')
        break
    except ValueError as error:
        print(error)
while True:
    try:
        inteirameia = int(input('Meia:\n 1 - {}R$\n Inteira:\n 2 - {}R$\n'.format('14:50', '29:00')))
        if not 1 <= inteirameia <= 2:
            raise ValueError('Digite um número correto')
        break
    except ValueError as error:
        print(error)
if inteirameia == 1:
   newvalor = '14:50'
   tipo = 'MEIA'
 else:
   newvalor = '29:00'
   tipo = 'INTEIRA'
if filme == "2":
 while True:
    try:
        hora = int(input('Selecione um horario p/ Adão Negro\n1 - {}\n2 - {}\n3 - {}\n'.format('13:20', '16:20', '18:20')))
        if not 0 <= hora <= 3:
            raise ValueError('Horario fora do intervalo permitido')
        break
    except ValueError as error:
        print(error)
while True:
    try:
        ingresso = int(input('Selecione o número de ingressos '))
        if ingresso == 0 or ingresso > 50:
           raise ValueError('Valor fora do intervalo permitido')
        break
    except ValueError as error:
        print(error)
while True:
    try:
        inteirameia = int(input('Meia:\n 1 - {}R$\n Inteira:\n 2 - {}R$\n'.format('14:50', '29:00')))
        if not 0 <= inteirameia <= 2:
    raise ValueError('Digite um número correto')
        break
    except ValueError as error:
        print(error)
if inteirameia == 1:
    newvalor = '14:50'
    tipo = 'MEIA'
else:
    newvalor = '29:00'
    tipo = 'INTEIRA'
if filme == "3":
while True:
        try:
            hora = int(input('Selecione um horario p/ Avatar\n1 - {}\n2 - {}\n3 - {}\n'.format('11:20', '22:45', '15:15')))
            if not 0 <= hora <= 3:
                raise ValueError('Valor fora do intervalo permitido')
            break
        except ValueError as error:
            print(error)

while True:
    try:
        ingresso = int(input('Selecione o número de ingressos '))
        if ingresso == 0 or ingresso > 50:
            raise ValueError('Valor fora do intervalo permitido')
        break
    except ValueError as error:
        print(error)

    while True:
        try:
            inteirameia = int(input('Meia:\n 1 - {}R$\n Inteira:\n 2 - {}R$\n'.format('14:50', '29:00')))
            if not 0 <= inteirameia <= 2:
                raise ValueError('Digite um número correto')
            break
        except ValueError as error:
            print(error)
            if inteirameia == 1:
                newvalor = '14:50'
                tipo = 'MEIA'
            else:
                newvalor = '29:00'
                tipo = 'INTEIRA'
print(50*'-')
if filme == '1' and hora == 1:
 newfilme = 'Pantera Negra'
 newhora = '14:20'
elif filme == '1' and hora == 2:
 newfilme = 'Pantera Negra'
 newhora = '15:35'
else:
 newfilme = 'Pantera Negra'
 newhora = '17:40'
if filme == '2' and hora == 1:
 newfilme = 'Adão Negro'
 newhora = '13:20'
elif filme == '2' and hora == 2:
 newfilme = 'Adão Negro'
 newhora = '16:40'
else:
 newfilme = 'Adão Negro'
 newhora = '18:20'
if filme == '3' and hora == 1:
 newfilme = 'Avatar'
 newhora = '11:20'
elif filme == '3' and hora == 2:
 newfilme = 'Avatar'
 newhora = '15:15'
else:
 newfilme = 'Avatar'
 newhora = '22:45'
print('Resumo:\nFILME: {}\nHORÁRIO: {}h\nINGRESSOS: {}\n VALOR: R${}\n TIPO: {}\n'.format(newfilme, newhora,ingresso, newvalor, tipo))
print(50 * '-')
print('Tenha um bom filme, {}!'.format(nome))

