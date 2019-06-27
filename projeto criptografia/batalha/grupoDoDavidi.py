from string import ascii_lowercase

alfabeto = list(ascii_lowercase)


def descriptografador(numero, key):
    for allP in range(len(numero)):
        for allA in range(len(alfabeto)):
            if(alfabeto[allA] == numero[allP]):
                allA = allA+key
                if allA < 0:
                    allA = allA+26
                    print(alfabeto[allA], '' + numero[allP], + allA)
                else:
                    if allA > 25:
                        allA = allA-26
                        print(alfabeto[allA], '' + numero[allP], + allA)
                    else:
                        print(alfabeto[allA], '' + numero[allP], + allA)


palavra = str(input('Digite o codigo: '))
keys = int(input('Digite a chave: '))

descriptografador(palavra, keys)