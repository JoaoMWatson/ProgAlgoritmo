from string import ascii_lowercase

alfabeto = list(ascii_lowercase)
resultado = []
arrayHexa = []

def criptografa(resultado):
    for i in resultado:
        arrayHexa.append(ord(i))
    return arrayHexa
            


palavra = str(input('palavra: '))
key = int(input('chave: '))



for allP in range(len(palavra)):
    for allA in range(len(alfabeto)):
        if(alfabeto[allA] == palavra[allP]):
            allA = allA-key
            resultado.append(alfabeto[allA])


resultado = resultado[::-1]
         
criptografa(resultado)
print(arrayHexa)

