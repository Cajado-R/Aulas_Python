nome = str(input('Diga-me seu nome ')).upper()
if nome == 'CLAUDIO':
    print('Que nome lindo')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é bem popular no Brasil')
elif nome in 'ANA CLAUDIA JESSICA JULIANA':
    print('Hm.. Belo nome feminino')
else:
    print('Seu nome é comum')
print('Tenha um bom dia, {}'.format(nome.lower()))
