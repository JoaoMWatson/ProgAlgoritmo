x = int(input('Digite o começo: '))
y = int(input('Digite o final: '))

if x > y:
    while x >= y:
        print(y)
        y += 1
elif x < y:
    while x <= y:
        print(x)
        x += 1
else:
    print('Os números são iguais')
print('Fim')
