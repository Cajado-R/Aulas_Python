lista = list()
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Qual a média de {aluno["nome"]} '))
if aluno['media'] > 7:
    aluno['situação'] = '\033[32mAprovado!!\033[m'
else:
    aluno['situação'] = '\033[31mReprovado'
lista.append(aluno)
for s in lista:
    for a, i in s.items():
        print(f'{a} é {i}')
if aluno['situação'] == '\033[32mAprovado!!\033[m':
    print(f'PARABÉNS {aluno["nome"]}')
