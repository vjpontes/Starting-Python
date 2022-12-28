#! python

palavra = 'paralelepido'
for letra in palavra:
    print(letra, end=',')

aprovados = ['rafa', 'pedro', 'joao']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

dias_semana = ('domingo', 'segunda', 'terca',
               'quarta', 'quinta', 'sexta', 'sabado')
for dia in dias_semana:
    print(f'hoje eh {dia}')

for numero in {1, 2, 3, 4}:
    print(numero)
