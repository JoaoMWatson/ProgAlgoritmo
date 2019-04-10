x = int(input('Digite um numero: '))

if x > 20:
    x -= 1
    while x > 20:
        print(x)
        x -= 1
elif x < 20:
    x += 1
    while x < 20:
        print(x)
        x += 1
else:
    print('Os Números são iguais')
print('Fim')