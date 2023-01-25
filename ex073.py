times = 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atletico-GO', 'Avaí', 'Juventude'
print(f'Os cinco primeiros times são: {times[0:5]}')
print(f'Os quatro últimos times são: {times[16:]}')
print(f'Em ordem alfabética seria: {sorted(times)}')
print(f'O time {times[4]} está na {times.index("Flamengo")+1}ª posição')