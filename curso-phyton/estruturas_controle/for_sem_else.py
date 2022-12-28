#! python

PALAVRAS_PROIBIDAS = ('futebol', 'politica', 'religião')
textos = {
    'joao gosta d futebol e politica',
    'a praia foi divertida'
}
for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('uma palavra proibida', palavra)
            found = True
            break

    if not found:
        print('texto liberado', texto)
