valores = []
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.append(pos, n)
                print(f'Adiconado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')