
'''lanche = [🍔, 🧃, 🍕, 🍨]'''
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Suco', 'Cookie']
print(lanche)
#insere em uma determinada posição o valor definido.
lanche.insert(0, 'Água')
print(lanche)
#Insere no final o valor declarado
lanche.append('Feijão')
print(lanche)
#Remove o item da posição declarada
del lanche[0]
print(lanche)
#remove o ultimo item
lanche.pop()
print(lanche)
#remove o item que você designou e também refatora a posição das chaves
lanche.remove('Suco')
print(lanche)
#A funlçao list cria uma lista nesse caso no range de 4 a 10
valores = list(range(4, 11))
print(valores)
numeros = [8, 2, 5, 4, 8, 3, 9, 1, 2, 5]
#Ordem crescente.
numeros.sort()
print(numeros)
#reverse ou seja ordem inversa, ou decrescente
numeros.sort(reverse=True)
print(numeros)


gat = []
for count in range(0, 5):
    gat.append(int(input('Digite um valor: ')))
for c, v in enumerate(gat):
    print(f'Na posição {c} encontrei o valor {v}!')


a = [2, 3, 5, 70]
#[:] cria uma copia dos itens da lista ao invés de fazer uma ligação dos itens, o que resultaria em uma ligação fazendo com que qualquer coisa que eu altere em uma seja alterada na outra
b = a[:]
b[2] = 8