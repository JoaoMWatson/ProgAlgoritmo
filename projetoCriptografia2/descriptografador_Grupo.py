from contextlib import suppress

with suppress(Exception):
    palavra = str(input("Digite o Codigo secreto e revele seu segredo: ")).strip().capitalize()
    fim = 3
    comeco = 0
    trio = 0

    for conjunto in palavra:
        trio = palavra[comeco:fim]
        trio = int(trio)
        print('{}'.format(chr(trio)), end='')
        comeco += 3
        fim += 3
