n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

maior1 = n1
if n2 > n3:
    while n2 < n1:
        print(n2)
        n2 += 1
else:
    while n3 < n1:
        print(n3)
        n3 += 1

maior2 = n2
if n1 > n3:
    while n3 < n2:
        print(n3)
        n3 += 1
else:
    while n1 < n2:
        print(n1)
        n1 += 1

maior3 = n3
if n1 > n2:
    while n1 < n3:
        print(n1)
        n1 += 1
else:
    while n2 < n3:
        print(n2)
        n3 += 1