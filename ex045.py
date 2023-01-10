import random
pc = ['pedra', 'papel', 'tesoura']
joken = random.choice(pc)
po = str(input('pedra? papel? ou tesoura?'))
if po == joken:
    print('EMPATE')
elif joken == 'pedra' and po == 'papel' or joken == 'papel' and po == 'tesoura' or joken == 'tesoura' and po == 'pedra':
    print('Você é um oponente digno e venceu a máquina!')
elif joken == 'tesoura' and po == 'papel' or joken == 'pedra' and po == 'tesoura' or joken == 'papel' and po == 'pedra':
    print('HAHAHAHAHAHAHA EU SOU A MELHOR MÁQUINA DO MUNDO')
