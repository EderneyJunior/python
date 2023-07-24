from time import sleep
def maior(*num):
    print('-='*15)
    print('Analizando valores...')
    for c in num:
        print(f'{c} ', end=' ', flush=True)
        sleep(0.5)
    print(f'foram informados, {len(num)} valores ao todo.')
    print(f'E o maior valor foi {max(num)}')


maior(5,0,9,8,15,20,5)
maior(2,6,50,100,102,54)
maior(0)
maior(0,1,2,3,4,5,6,7,8,9,10)
