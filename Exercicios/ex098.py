from time import sleep
def linha():
    print('-=' * 30)
    for c in range(10, -1, -2):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
def cont(i, f, p):
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p > 0:
        for c in range(i, f+1, p):
            print(c, end=' ', flush=True)
            sleep(0.5)
    else:
        for c in range(i, f-1, p):
            print(c, end=' ', flush=True)
            sleep(0.5)
linha()
cont()
linha()
cont()
linha()
print('Agora é sua vez de personalizar a contagem!')
cont(int(input('Inicio: ')), 
     int(input('Fim: ')),
     int(input('Passo: ')))