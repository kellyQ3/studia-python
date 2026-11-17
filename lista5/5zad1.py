def F(n):
    if n % 2 == 0:
        return n / 2 
    else:
        return 3 * n + 1


def energia(n):
    kroki = 0
    while n != 1: 
        n = F(n)
        kroki += 1
    return kroki


def analiza_collatza(a, b):
    lista_energii = []
    for x in range(a, b + 1):
        lista_energii.append(energia(x))

    srednia = sum(lista_energii) / len(lista_energii)

    posortowana = sorted(lista_energii)
    n = len(posortowana)
    if n % 2 == 1:
        mediana = posortowana[n // 2]
    else:
        mediana = (posortowana[n // 2 - 1] + posortowana[n // 2]) / 2

    print(f"Energie: {lista_energii}")
    print(f"Średnia energia: {srednia:.2f}")
    print(f"Mediana energii: {mediana}")
    print(f"Minimalna energia: {min(lista_energii)}")
    print(f"Maksymalna energia: {max(lista_energii)}")


analiza_collatza(1, 7)