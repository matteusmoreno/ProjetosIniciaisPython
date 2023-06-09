from time import sleep

for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;31mBUM ...\033[m \033[1;33mPOW ...\033[m \033[1;35mPOW\033[m')
