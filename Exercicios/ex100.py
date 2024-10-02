from random import randint
from time import sleep
números = []
def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        números.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')
# def somaPar():
sorteia(números)
