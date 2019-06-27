n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n2 > n3:
    while n2 < n1:
        print(n2)
        n2 += 1
elif n1 > n3 :
    while n3 < n1:
        print(n3)
        n3 += 1

elif n2 > n1 and n1 > n3:
    while n1 < n2:
        print(n1)
        n1 += 1
elif n2 > n3:
    while n3 < n2:
        print(n3)
        n3 += 1

elif n3 > n1 and n1 > n2:
    while n1 < n3:
        print(n1)
        n1 += 1
elif n3 > n2 :
    while n2 < n3:
        print(n2)
        n2 += 1
else:
    print('Os Numeros são iguais')

print('FIM!!!')