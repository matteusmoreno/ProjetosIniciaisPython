s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s += num
        cont += 1
print('Ao todo foram {} números \033[1mPARES\033[m e a \033[1mSOMA\033[m é: {}'.format(cont, s))

