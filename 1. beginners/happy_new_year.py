import colorama
from colorama import Fore
colorama.init()

# My Christmas tree
print(Fore.GREEN + ' ' * 39 + Fore.LIGHTRED_EX + '</>')
for i in range(1, 36):
    if i % 11 != 0:
        print(Fore.GREEN + ' ' * int(40 - i) + i * '*', end='|')
        print(Fore.GREEN + i * '*')
    else:
        print(Fore.LIGHTYELLOW_EX + ' ' * (41 - i) + 'Happy New Python Year!' * (i // 11))