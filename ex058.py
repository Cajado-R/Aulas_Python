import random
escolhadopc = random.randrange(10)
print(escolhadopc)
tentou = 0
escolhadocliente = 999
nvescolhadocliente = 0
while escolhadopc != escolhadocliente:
    nvescolhadocliente = int(input('\033[1:31mDe 0 a 10 qual número você acha que eu pensei? '))
    print('\033[1:31mERROU!')
    escolhadocliente = nvescolhadocliente
    tentou += 1
if escolhadopc == nvescolhadocliente:
    print('\033[1:32mVocê finalmente me venceu, com \033[1:34m{} \033[1:32mtentativas!!'.format(tentou))

