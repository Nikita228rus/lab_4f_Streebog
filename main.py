from work_func import *
import time


def menu():
    case = input('1 - ввод из консоли\n2 - чтение из файла\n>>>\t')
    if case == '1':
        massive = input('Введите текст:\t')

    elif case == '2':
        with open("input.txt", "r") as file:
            massive = file.read()

    massive = hex_bin(reverse(text_to_hex(text_to_bin(massive))))

    choose = input('Выбор свертки\n512 - 1\n256 - 2\n>>>\t')
    if choose == '1':
        final = stribog_256_512(massive, 1)
        with open("output.txt", "a", encoding='utf-8') as file:
            file.write('512: {}\ntime:\t{}\n\n'.format(final, time.asctime()))

    elif choose == '2':
        final = stribog_256_512(massive, 2)
        with open("output.txt", "a", encoding='utf-8') as file:
            file.write('256: {}\ntime:\t{}\n\n'.format(final, time.asctime()))


menu()
