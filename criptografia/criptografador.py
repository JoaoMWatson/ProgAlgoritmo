from string import ascii_lowercase
from time import sleep

alphabeto = list(ascii_lowercase)
x = 0
pronto = []


def descriptografar(numeros):
    for i in numeros:
        x = numeros.split(i)
        x = int(i)
        pronto.append(alphabeto[x])
        for x in pronto:
            print(f'{x}', end='')
            pronto.remove(x)


print('~-' * 40)
print('SUPER PROGRAMA DE CRIPTOGRAFIA UHUUUUL')
print('~-' * 40)

print("""MENU
1- Descriptografador 
2- Criptografador
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
    print( '-=' * 40)
    print('Descriptografador 2000')
    print('-=' * 40)

    numeros = (str(input('Digite o codigo que sera descriptografado: '))).strip()
    print(f'A mensagem secreta é: {descriptografar(numeros)}')

elif opcao == 2:
    print('-=' * 40)
    print('Criptografador 2000')
    print('-=' * 40)

elif opcao == 0:
    print('Encerrando o programa')
    print('Obrigado por escolher nossos serviços ^^')
    exit

else:
    print('Opção invalida: ')
