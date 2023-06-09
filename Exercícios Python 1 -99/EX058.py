from random import randint
computador = randint(0, 10)
resp = -1
cont = 0
print('Olá, sou seu computador\nAcabei de pensar num número entre 0 e 10, tente adivinhar!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
while resp != computador:
    while True:
        resp_str = input('Qual é o seu palpite? ')
        if resp_str.isdigit():
            resp = int(resp_str)
            break
        else:
            print('\033[1;31mVocê digitou uma alternativa inválida. Tente novamente.\033[m')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    cont += 1
    if -1 < resp < 11:
        if computador < resp:
            print('\033[1;33mMenos... tente mais uma vez\033[m')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        elif computador > resp:
            print('\033[1;33mMais... tente mais uma vez\033[m')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    else:
        print('\033[1;31mVocê digitou uma alternativa inexistente. Tente novamente.\033[m')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
if cont == 1:
    print('\033[1;32mParabéns, você acertou com {} tentativa\033[m'.format(cont))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
else:
    print('\033[1;32mParabéns, você acertou com {} tentativas\033[m'.format(cont))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
