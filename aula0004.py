car = int(input("Digite a quanto tempo você possui o seu carro: "))
if car <= 3:
    print('Carro novo')
elif car > 4 and car < 10:
    print('Esse carro já tá mais velhinho ')
else:
    print('Seu carro já tem mais de 10 anos e isso é muito tempo')