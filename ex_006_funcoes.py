def media(nota1, nota2):
    return (nota1 + nota2) / 2


def mostrar(med):
    if med >= 6:
        print("Aprovado com média ", med)
    elif med > 2:
        print("Recuperação com média ", med)
    else:
        print("Reprovado com média ", med)
