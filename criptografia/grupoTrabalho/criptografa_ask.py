arrayHexa = []

def criptografa(palavra):
    for i in palavra:
        x = palavra.split(i)
        x = str(i)

        arrayHexa.append(ord(x))
        for x in arrayHexa:
            print(f'{x}', end='')
            arrayHexa.remove(x)

palavra = (str(input('Digite a frase que sera criptofrafada: '))).strip()
criptografa(palavra)