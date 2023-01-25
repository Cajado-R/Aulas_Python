import random
'''    numeros1 = random.randint(0, 100)
    numeros2 = random.randint(0, 100)
    numeros3 = random.randint(0, 100)
    numeros4 = random.randint(0, 100)
    numeros5 = random.randint(0, 100)
    numerol = numeros1, numeros2, numeros3, numeros4, numeros5'''
numerol = ((random.randint(0, 100)), (random.randint(0, 100)), (random.randint(0, 100)),
         (random.randint(0, 100)), (random.randint(0, 100)))
maior = numerol[0]
if maior < numerol[1]:
    maior = numerol[1]
if numerol[2] > maior:
    maior = numerol[2]
if numerol[3] > maior:
    maior = numerol[3]
if numerol[4] > maior:
    maior = numerol[4]
menor = numerol[0]
if menor > numerol[1]:
    menor = numerol[1]
if menor > numerol[2]:
    menor = numerol[2]
if menor > numerol[3]:
    menor = numerol[3]
if menor > numerol[4]:
    menor = numerol[4]
print(f'o maior número foi: {maior}')
print(f'O menor número foi: {menor}')
print(f'A sequência foi: {numerol}')
