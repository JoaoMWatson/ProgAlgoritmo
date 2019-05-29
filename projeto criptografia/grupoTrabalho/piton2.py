from string import ascii_lowercase
from time import sleep

alfabeto = list(ascii_lowercase)
x = 0
pronto = []
arrayPalavra = []
arrayHexa = []
key = 0


def descriptografar(numero, key):
    for allP in range(len(numero)):
        for allA in range(len(alfabeto)):
            if(alfabeto[allA] == numero[allP]):
                allA=allA+key
                if allA<0:
                    allA=allA+26
                    print(alfabeto[allA],''+ numero[allP], + allA)
                else:
                    if allA>25:
                        allA=allA-26
                        print(alfabeto[allA],''+ numero[allP], + allA)
                    else:
                        print(alfabeto[allA],''+ numero[allP], + allA)
            

def criptografa(palavra, key):
    for allP in range(len(palavra)):
        for allA in range(len(alfabeto)):
            if(alfabeto[allA] == palavra[allP]):
                allA=allA-key
                if allA<0:
                    allA=allA+26
                    print(palavra[allP],''+ alfabeto[allA], + allA)
                else:
                    if allA>25:
                        allA=allA-26
                        print(palavra[allP],''+ alfabeto[allA], + allA)
                    else:
                        print(palavra[allP],''+ alfabeto[allA], + allA)

                        
def descriptografador_auto(numero):
    c=0
    for k in range(26):
        for j in range(len(numero)):
            for i in range(len(alfabeto)):
                if (alfabeto[i] == numero[j]):
                    i=c-26+i
                    print('{}'.format(alfabeto[i]), end='')
        print("\n--------")
        c=c+1

        
def criptografa_hexa(palavra):
    for i in palavra:
        x = palavra.split(i)
        x = str(i)

        arrayHexa.append(ord(x))
        for x in arrayHexa:
            print('{}'.format(arrayHexa), end='')
            arrayHexa.remove(x)
                    

print('~-' * 40)
print('SUPER PROGRAMA DE CRIPTOGRAFIA UHUUUUL')
print('~-' * 40)

print("""MENU
1- Criptografador
2- Descriptografador
3- Descriptografador Automatico xD
4- Criptografador Asc ii
0- Sair.
    """)


opcao = int(input('Selecione uma opção: '))
print('Processando informação', end='', flush='True')
while x < 4:
    print('.', end='', flush='True')
    x += 1
    sleep(0.3)


if opcao == 1:
    print('\n')
    print('-=' * 40)
    print('Criptografador 2000')
    print('-=' * 40)

    palavra = input("Digite uma palavra: ")
    key = int(input("Digite uma chave: "))
    criptografa(palavra, key)

elif opcao == 2:
    print('\n')
    print('-=' * 40)
    print('Descriptografador 2000')
    print('-=' * 40)

    numero = (str(input('Digite o codigo que sera descriptografado: '))).strip()
    key = int(input("Digite uma chave: "))
    print("Mensagem descriptografada é: ")
    descriptografar(numero,key)

elif opcao == 3:
    print('\n')
    print('-=' * 40)
    print('Descriptografador 3000')
    print('-=' * 40)

    numero = (str(input('Digite o codigo que sera descriptografado: '))).strip()
    descriptografador_auto(numero)

elif opcao == 4:
    print('\n')
    print('-=' * 40)
    print('Criptografador 3000')
    print('-=' * 40)

    palavra = input("Digite uma palavra: ")
    criptografa_hexa(palavra)
    
elif opcao == 0:
    print('Encerrando o programa')
    print('Obrigado por escolher nossos serviços ^^')
    exit

else:
    print('Opção invalida: ')
