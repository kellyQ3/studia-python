def is_prime(n):
    if n < 2:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    return True
        
def dzielniki_pierwsze(liczba):
    zbior = set()
    for dzielnik in range(2,liczba+1):
        if liczba % dzielnik == 0 and is_prime(dzielnik):
            zbior.add(dzielnik)
    return zbior

print(dzielniki_pierwsze(100))