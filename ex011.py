#área, 2m² tinta
alt = float(input('Digite o valor da altura da parede'))
larg = float(input('Digite o valor da largura da parede'))
print('A área da parede é de {}m² e será necessario {}l de tinta para pintar a parede '.format(alt*larg, (alt*larg)/2))