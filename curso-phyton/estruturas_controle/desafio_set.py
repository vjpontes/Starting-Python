PALAVRAS_PROIBIDAS = {'futebol', 'politica', 'religião'}
textos = {
    'joao gosta d futebol e politica',
    'a praia foi divertida'
}

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('texto proibido', intersecao)
    else:
        print('texto autorizado', texto)
