name = str(input('Digite o nome do aluno'))
n1 = float(input('Digite a primeira Nota '))
n2 = float(input('Digite a segunda Nota '))
print('\033[1;47mO aluno {}\n obteve como média {}\033[m'.format(name, (n1+n2)/2))