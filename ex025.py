nome = input('Digite o seu nome: ').upper()
name = nome.split()
print('Você se chama {} possui Silva no nome? {}'.format(name, 'SILVA' in name))
