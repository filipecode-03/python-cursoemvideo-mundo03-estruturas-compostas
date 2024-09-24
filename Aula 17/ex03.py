num = [2, 5, 9, 1]
num[2] = 3
print(num)

num2 = num[:] 
num.append(7)
print(num2)

num3 = num[:]
num.sort(reverse=True)
print(num3)
num.insert(2, 2)
num.pop(2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
num.remove(4)
print(num)
print(f'Essa lista tem {len(num)} elementos')