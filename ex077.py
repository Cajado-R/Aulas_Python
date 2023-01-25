lista = 'hamburguer', 'peito de frango', 'pizza', 'caldo de cana', 'pastel', 'batata frita'
'''vogal = "aeiou"
for palavra in lista:
    for vogais in vogal:
        qtd = palavra.count(vogais)
        if qtd > 0:
            print(f'Na palavra {palavra} temos {qtd} vogal(is) {vogais}')'''
for p in lista:
    print(f'\nNa palavra {p} temos',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f' {letra}',end='')