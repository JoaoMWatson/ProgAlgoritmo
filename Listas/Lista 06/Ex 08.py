x = int(input('Digite um numero menor que 5(Cinco): '))
while x >= 5:
    x = int(input('Numero maior que cinco, favor digitar novamente: '))

if x % 2 == 0:
    while x < 20:
        print(x)
        x += 2
else:
    x += 1
    while x < 20:
        print(x)
        x += 2

print('FIM!!')
        