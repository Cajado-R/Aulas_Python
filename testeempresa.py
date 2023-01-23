#k = fase de grupo -- (2) n = times (quantos?)
equipe1 = int(input('Quantos gols fez a primeira equipe: '))
equipe2 = int(input('Quantos gols fez a segunda equipe: '))
equipe3 = int(input('Quantos gols fez a terceira equipe: '))
equipe4 = int(input('Quantos gols fez a quarta equipe: '))
arr = [equipe1, equipe2, equipe3, equipe4]
#organização dos grupos usando sorted dentro da array para evitar o calculo
reorganizacao = sorted(arr)
#pegando as equipes 0 e 1 dentro da array depois de organizadas para calcular a diferença de gols
k = [reorganizacao[0], reorganizacao[1]]
if reorganizacao[0] > reorganizacao[1]:
    #para evitar erros como número negativo na diferença de gols fiz um if e um else em cada grupo
    diferenca_de_gols = int(reorganizacao[0]) - int(reorganizacao[1])
else:
    diferenca_de_gols = int(reorganizacao[1]) - int(reorganizacao[0])
k1 = [reorganizacao[2], reorganizacao[3]]
if reorganizacao[2] > reorganizacao[3]:
    diferenca_de_gols1 = int(reorganizacao[2]) - int(reorganizacao[3])
else:
    diferenca_de_gols1 = int(reorganizacao[3]) - int(reorganizacao[2])
print(f'O primeiro grupo será composto das equipes {k}')
print(f'A diferença de gols entre o grupo 1 é de {diferenca_de_gols} gol(s)')
print(f'E o segundo grupo será composto das equipes {k1}')
print(f'A diferença de gols entre o grupo 2 é de {diferenca_de_gols1} gol(s)')