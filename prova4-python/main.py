n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))


def media(n1, n2, n3):
    media_de_notas = (n1+n2+n3) / 3
    return f'A sua média foi {media_de_notas:.2f}'


print(media(n1, n2, n3))