def podziel(s):
    napis = []
    slowo = ""
    for znak in s:
        if znak.isspace() == False:
            slowo += znak
        elif slowo != "":
                napis.append(slowo)
                slowo = ""
    if slowo != "":
        napis.append(slowo)
    return napis

print(podziel(" Ala      ma      kota aaa"))
print(podziel("   \t\n  "))
print(podziel(""))
print(podziel("Ala\tma\nkota"))
