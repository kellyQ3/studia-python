def usun_duplikaty(L):
    if not L:
        return []

    pary = []
    for i in range(len(L)):
        pary.append([L[i], i])

    pary.sort()

    bez_duplikatow = [pary[0]]
    for i in range(1, len(pary)):
        if pary[i][0] != pary[i - 1][0]:
            bez_duplikatow.append(pary[i])
            
    odwrocone = []
    for para in bez_duplikatow:
        odwrocone.append([para[1], para[0]])
    odwrocone.sort()

    wynik = []
    for para in odwrocone:
        wynik.append(para[1])

    return wynik


lista = [1, 2, 3, 1, 2, 3, 8, 2, 2, 2, 9, 9, 4]
print(usun_duplikaty(lista))  