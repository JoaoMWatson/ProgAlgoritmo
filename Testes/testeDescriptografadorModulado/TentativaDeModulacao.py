from contextlib import suppress
from string import ascii_lowercase

with suppress(Exception):

    def asciiInAlphanum(palavra):
        resultado = []
        fim = 3
        comeco = 0
        trio = 0
        for conjunto in palavra:
            trio = palavra[comeco:fim]
            trio = int(trio)
            resultado.append(chr(trio))
            print('{}'.format(chr(trio)), end='')
            comeco += 3
            fim += 3


def descriptografador(resultado, key):
    alfabeto = list(ascii_lowercase)
    resultado = []
    for indexResultado in range(len(resultado)):
        for letraAlfabeto in range(len(alfabeto)):
            if(alfabeto[letraAlfabeto] == resultado[indexResultado]):
                letraAlfabeto = letraAlfabeto+key
                if letraAlfabeto < 0:
                    letraAlfabeto = letraAlfabeto+26
                    return alfabeto[letraAlfabeto], '' + resultado[indexResultado], + letraAlfabeto
                else:
                    if letraAlfabeto > 25:
                        letraAlfabeto = letraAlfabeto-26
                        return alfabeto[letraAlfabeto], '' + resultado[indexResultado], + letraAlfabeto
                    else:
                        return alfabeto[letraAlfabeto], '' + resultado[indexResultado], + letraAlfabeto
