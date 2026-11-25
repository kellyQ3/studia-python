with open("slowa.txt", encoding="utf-8") as plik:
    lista_slow = []
    for linia in plik:
        slowo = linia.strip()
        if slowo:
            lista_slow.append(slowo)
zbior_slow = set(lista_slow)
for slowo in lista_slow:
    odwrocone = slowo[::-1]
    if odwrocone in zbior_slow and slowo < odwrocone:
        print(slowo, "=", odwrocone)
#lista->set by zachowac kolejnosc