import random
escolha = random.randrange(6)
qualvoceacha = int(input("Adivinhe o número escolhido de 0 a 5: " ))
if escolha == qualvoceacha:
    print('Nossa você é bom nisso, porém gastou toda a sua sorte :c ')
else:
    print('Você errou')