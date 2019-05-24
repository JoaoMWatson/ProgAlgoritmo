
from string import ascii_lowercase

alphabeto = list(ascii_lowercase)

pronto = []

def descriptografar(numeros):
    for i in numeros:
        x = numeros.split(i)
        x = int(i)
        pronto.append(alphabeto[x])
        for x in pronto:
            print(f'{x}', end='')
            pronto.remove(x)


numeros = (str(input('Digite o codigo que sera descriptografado: '))).strip()


print(numeros)
descriptografar(numeros)
