jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for cont in range(tot):
    partidas.append(int(input(f'        Quantos gols na partida {cont}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)