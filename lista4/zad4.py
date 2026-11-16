def erastotenes(n):
    L = list(range(n + 1))
    L[0] = 0
    L[1] = 0
    for p in range(2, int(n**0.5) + 1):
        if L[p] != 0:
            for i in range(p * p, n + 1, p):
                L[i] = 0
    return L
def czy_palindrom(n):
    s = str(n)
    return s == s[::-1]

def palindromy(a, b):
    liczby = erastotenes(b)
    wynik = []
    
    for x in liczby:
        if x >= a and x != 0 and czy_palindrom(x):
            wynik.append(x)
            
    return wynik

print(palindromy(1, 1000))