teste = list()
teste.append('Cláudio')
teste.append(25)
galera = list()
galera.append(teste[:])
teste[0] = 'André'
teste[1] = 27
galera.append(teste[:])
print(galera)

galera = [['João', 22], ['Lucas', 12], ['Cláudio', 15], ['Andrew', 13]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
#pegando todos os itens dentro da estrutura de dados
print(galera)
#pegando item dentro da lista
print(galera[0][1])
galera.clear()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    print(galera)
totmai = totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        totmen += 1
print(f'O número de menores de idade é {totmen}, e o número de maiores de idade é {totmai}')