numero = valoresdigitados = soma = 0
#enquanto diferente de 999
while True:
    numero = int(input('Digite um valor [999 PARA]'))
    # condição de parada
    if numero == 999:
    #o que faz parar ↓
        break
        #número q foram obtidos adicionados a soma sem o 999 pois foi parado acima
    soma += numero
    valoresdigitados += 1
print(f'A soma dos {valoresdigitados} valores digitados resultou na soma de:  {soma}')