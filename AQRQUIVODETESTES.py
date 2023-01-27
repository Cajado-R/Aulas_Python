filmes = {
    'Pantera Negra':{
        'faixa': 15,
        'horario':['12:20','14:30']
        },
    'Adao Negro':{
        'faixa': 18,
        'horario':['22:00','00:30']
        },
}
print('bem vindo a lucafilm\nhoje temos estes magnificos filmes')
print(list(filmes.keys()))
idade = int(input('qual sua idade'))
for filme,detalhes in filmes.items():
    if  idade >= detalhes['faixa']:
        print(filme ,end=', ')