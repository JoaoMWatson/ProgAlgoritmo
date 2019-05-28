
from string import ascii_lowercase

alphabeto = list(ascii_lowercase)

sep_um = []


def descriptografar(numeros):
    for i in numeros:
        x = numeros.split(i)
        x = int(i)
        sep_um.append(alphabeto[x])

        for x in sep_um:
            print(f'{x}', end='')
            sep_um.remove(x)


print(sep_um)
numeros = (str(input('Digite o codigo que sera descriptografado: '))).strip()
print('O codigo descritografado é: ', end='')
descriptografar(numeros)
