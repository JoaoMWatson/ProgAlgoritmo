from contextlib import suppress
from string import ascii_lowercase

with suppress(Exception):

    fim = 3
    comeco = 0
    trio = 0
    alfabeto = list(ascii_lowercase)
    resultado = []

    def ascii_in_alphnum(palavra):
        for conjunto in palavra:
            trio = palavra[comeco:fim]
            trio = int(trio)
            resultado.append(chr(trio))

            comeco += 3
            fim += 3


def descriptografador(resultado, key):
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


palavra = str(
    input("Digite o Codigo secreto e revele seu segredo: ")).strip().lower()
key = int(input('Descubra a chave para descriptografar, coloque-a aqui: '))
resultadoFinal = descriptografador(ascii_in_alphnum(palavra), key)

print('O secredo a ser revelado é {}'.format(resultadoFinal[::-1]))
