numero = valoresdigitados = soma = 0
#enquanto diferente de 999
while numero != 999:
    numero = int(input('Digite um valor [999 PARA]'))
    valoresdigitados += 1
    # condição de parada
    if numero == 999:
        valoresdigitados -= 1
    #o que faz parar ↓
        break
        #número q foram obtidos adicionados a soma sem o 999 pois foi parado acima
    soma += numero
print(f'A soma dos {valoresdigitados} valores digitados resultou na soma de:  {soma}')