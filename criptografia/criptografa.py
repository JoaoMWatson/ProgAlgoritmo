from string import ascii_lowercase

alphabeto = list(ascii_lowercase)
print(alphabeto)
arrayPalavra = []

def criptografa(palavra):
    for i in palavra:
        x = palavra.split(i)
        x = str(i)
        index = alphabeto.index(x)
        arrayPalavra.append(index)
        for x in arrayPalavra:
            print(f'{x}', end='')
            arrayPalavra.remove(x)

palavra = (str(input('Digite a frase que sera criptofrafada: '))).strip()
print(arrayPalavra)

print(f'A sua frase criptografada ficou: ', end='')
criptografa(palavra)
