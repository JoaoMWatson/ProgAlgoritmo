x = int(input('Digite um numero maior que 10(Dez): '))
y = int(input('Digite um numero menor que 5(Cinco): '))

while x <= 10:
    x = int(input('Numero menor que dez, favor digitar novamente: '))
while y >= 5:
    y = int(input('Numero maior que cinco, favor digitar novamente: '))

print(x, y)
print('FIM!!')