#área, 2m² tinta
alt = float(input('Digite o valor da altura da parede'))
larg = float(input('Digite o valor da largura da parede'))
print('\033[1;47mA área da parede é de {}m² e será necessario {}l de tinta para pintar a parede \033[m'.format(alt*larg, (alt*larg)/2))