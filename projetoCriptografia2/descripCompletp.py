from contextlib import suppress
from contentDescrip import descriptografador, asciiInAlphanum
from time import sleep


with suppress(Exception):
    palavra = str(
        input("Digite o Codigo secreto e revele seu segredo: "))
    key = int(input('Digite a chave misteriosa para o codigo: '))

    resultadoFinal = descriptografador(asciiInAlphanum(palavra), key)

    print('O secredo será revelado')
    sleep(1)
    print('-=' * (len(resultadoFinal) + 2))
    print(f'A palavra é {resultadoFinal}')
    print('-=' * (len(resultadoFinal) + 2))