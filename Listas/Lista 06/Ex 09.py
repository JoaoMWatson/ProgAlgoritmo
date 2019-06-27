from time import sleep

print('=' * 30)
print('Contagem Regressiva')
print('=' * 30)

x = int(input('Digite um numero maior que 20(Vinte): '))

while x <= 20:
    x = int(input('Numero menor que vinte, favor digitar novamente: '))

while x > 1:
    print(x)
    x -= 1
    sleep(0.3)

print('BUM POOW CATAPUMM!!!')