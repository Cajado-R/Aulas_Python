num = 0
lista = list()
while num < 5:
    nume = int(input("Digite um número: "))
    for i in range(len(lista)):
        if nume < lista[i]:
            lista.insert(i, nume)
            break
    else:
        lista.append(nume)
    num += 1
print(lista)
