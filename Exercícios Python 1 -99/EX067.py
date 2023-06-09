while True:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    num = int(input('Quer ver tabuada de qual valor? '))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    if num < 0:
        print('\033[1;34mPROGRAMA TABUADA ENCERRADO!\033[m')
        break
    c = 0
    while 0 <= c <= 9:
        c += 1
        res = c * num
        print(f'{c}  x  {num} = {res}')








