nomes = []
notas = []

for i in range(5):
    nomes.append(input('Informe o nome do aluno: '))
    notas.append(eval(input(f'informe a nota do aluno ' + nomes[i] + ': ')))
    i += 1
print('-=' * 50)


for x in range(5):
    print(f'O aluno: {nomes[x]} teve nota: {notas[x]}')
print('-=' * 50)


media = 0
for x in range(5):
    media += notas[x]
    x += 1
total = media / 5
print('A media dos alunos é: {}'.format(total))
print('-=' * 50)


for x in range(5):
    if notas[x] > total:
        print(f'O aluno {nomes[x]} teve a nota {notas[x]} e ficou acima da media')    


print('-=' * 50)
print('Fim!!')

