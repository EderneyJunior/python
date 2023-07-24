import random
import time

usuario = int(input('[ 1 ] Pedra\n[ 2 ] papel\n[ 3 ] tesoura\nQual sua escolha? '))
pc = random.randint(1,3)

print(f'JO')
time.sleep(1)
print(f'KEN')
time.sleep(1)
print(f'PO!!!\n')

if usuario == pc:
    print(f'\033[34mEMPATE!\033[m')
elif usuario == 1 and pc == 3:
    print(f'\033[32mVITÓRIA!\033[m\nO usuario escolheu pedra e o pc escolheu tesoura')
elif usuario == 3 and pc == 2:
    print(f'\033[32mVITÓRIA!\033[m\nO usuario escolheu tesoura e o pc escolheu papel')
elif pc == 1 and usuario == 3:
    print(f'\033[31mDERROTA!\033[m\nO usuario escolheu tesoura e o pc escolheu pedra')
elif pc == 3 and usuario == 2:
    print(f'\033[31mDERROTA!\033[m\nO usuario escolheu papel e o pc escolheu tesoura')
print(f'FIM')
