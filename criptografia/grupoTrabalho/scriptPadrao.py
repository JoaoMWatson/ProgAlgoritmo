from string import ascii_lowercase, ascii_uppercase

alphabeto = list(ascii_lowercase+ascii_uppercase)
palavra = str(input('Digite a palavra a ser criptografada'))
key = int(input('Digite a chave da criptografia'))

for allP in range(len(palavra)):
    for allA in range(len(alphabeto)):
        if(alphabeto[allA] == palavra[allP]):
            allA=allA+key
            if allA<0:
                allA=allA+26
                print(palavra[allP], '' + alphabeto[allA], + allA)
            else:
                if allA>25:
                    allA=allA-26
                    print(palavra[allP], '' + alphabeto[allA] + allA)
                else:
                    print(palavra[allP], '' + alphabeto[allA], + allA)
