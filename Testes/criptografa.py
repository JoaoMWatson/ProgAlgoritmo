from string import ascii_lowercase

alphabeto = list(ascii_lowercase)
print(alphabeto)
arrayPalavra = []

def criptografa(palavra, key):
    for i in palavra:
        x = palavra.split(i)
        x = str(i)
        index = alphabeto.index(x)
        arrayPalavra.append(index)
        for x in arrayPalavra:
            print(f'{x}', end='')
            arrayPalavra.remove(x)


palavra = (str(input('Digite a frase que sera criptofrafada: '))).strip()
key = int(input('Digite a chave da criptografia: '))

print(f'A sua frase criptografada ficou: ', end='')

