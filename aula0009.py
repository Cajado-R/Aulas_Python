lanche = 'pizza', 'suco', 'hamburguer', 'sorvete'
for c in (lanche):
    print(c, end=' ')
while True:
    print(lanche, end=' ')
    break
print(lanche[0], end=' ')
for c in range(0, len(lanche)):
    print(f'{lanche[c]}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche))