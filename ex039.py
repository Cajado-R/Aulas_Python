'''Teste do ebmil'''
from datetime import date
anodehoje = date.today()
anodeh = anodehoje.year
seunome = str(input('Digite seu nome completo, por favor: ' ))
anonasc = int(input('Digite seu ano de nacimento ex(2010): '))
idade = (anodeh - anonasc)
if idade < 18:
    print('Ainda não está no ano de você se alistar, você tem {} e faltam {} anos para você se alistar'.format(idade, 18 - idade))
elif idade > 18:
    print('Já passou da hora de você se alistar, passaram {} anos do seu ano de alistamento'.format(idade - 18))
elif idade == 18:
    print('Você precisa ir se alistar')
