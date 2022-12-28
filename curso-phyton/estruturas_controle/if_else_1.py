#! phyton

def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        return 'nota invalida'
    elif nota >= 9.1:
        return 'a'
    elif nota >= 8.1:
        return 'a-'
    elif nota >= 7.1:
        return 'b'
    elif nota >= 6.1:
        return 'b-'
    elif nota >= 5.1:
        return 'c'
    elif nota >= 4.1:
        return 'c-'
    elif nota >= 3.1:
        return 'd'
    elif nota >= 2.1:
        return 'd-'
    elif nota >= 1.1:
        return 'e'
    elif nota >= 0:
        return 'e-'
    else:
        return 'nota invalida'


if __name__ == '__main__':
    valor_informado = input('valor daa nota ')
    conceito = nota_conceito(valor_informado)
    print(conceito)
