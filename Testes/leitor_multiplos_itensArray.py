from contextlib import suppress
# Ignora o erro
with suppress(Exception):
    variavel = str(input('digita numero: '))
    x = 3
    y = 0
    guardar = 0

    for trio in variavel:
        guardar = variavel[y:x]
        guardar = int(guardar)
        print('{}'.format(chr(guardar)), end='')
        y += 3
        x += 3
