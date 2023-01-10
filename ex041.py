'''Nadadores até 9 anos mirim até 14 infantil até 19 junior até 20 senior mais que isso master'''
from datetime import date
anodehoje = date.today()
anodeh = anodehoje.year
print(35*'-')
print('CONFEDERAÇÃO BRASILEIRA DE NATAÇÃO')
print(35*'-')
anodenascimento = int(input('Digite seu ano de nascimento: '))
idade = anodeh - anodenascimento
if idade <= 9:
    print('Atleta \033[1:31mMIRIM')
elif idade <= 14:
    print('Atleta \033[1:31mINFATIL')
elif idade <= 19:
    print('Atleta \033[1:31mJÚNIOR')
elif idade <= 20:
    print('Atleta \033[1:31mSENIOR')
else:
    print('Atleta \033[1:31mMASTER')


