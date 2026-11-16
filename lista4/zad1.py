import turtle

t = turtle.Turtle()
t.speed(0)  
turtle.colormode(255)

def kwadrat(rozmiar, kolor):
    t.color("black", kolor)
    t.begin_fill()
    for _ in range(4):
        t.forward(rozmiar)
        t.left(90)
    t.end_fill()

def rysuj_spirale(poczatkowe_n):
    kolor_start = (214, 51, 132)  
    kolor_koniec = (255, 255, 0)   
    rozmiar = 15 
    n = poczatkowe_n
    
    calkowita_liczba_kwadratow = sum(range(1, poczatkowe_n + 1))
    indeks_kwadratu = 0
    
    for i in range(poczatkowe_n):
        for _ in range(n - 1):
            proporcja = indeks_kwadratu / max(1, calkowita_liczba_kwadratow - 1)
            r = int(kolor_start[0] + (kolor_koniec[0] - kolor_start[0]) * proporcja)
            g = int(kolor_start[1] + (kolor_koniec[1] - kolor_start[1]) * proporcja)
            b = int(kolor_start[2] + (kolor_koniec[2] - kolor_start[2]) * proporcja)
            aktualny_kolor = (r, g, b)
            
            kwadrat(rozmiar, aktualny_kolor)
            indeks_kwadratu += 1
            t.left(90)
            t.forward(rozmiar)
            t.right(90)

        proporcja = indeks_kwadratu / max(1, calkowita_liczba_kwadratow - 1)
        r = int(kolor_start[0] + (kolor_koniec[0] - kolor_start[0]) * proporcja)
        g = int(kolor_start[1] + (kolor_koniec[1] - kolor_start[1]) * proporcja)
        b = int(kolor_start[2] + (kolor_koniec[2] - kolor_start[2]) * proporcja)
        aktualny_kolor = (r, g, b)
        
        kwadrat(rozmiar, aktualny_kolor)
        indeks_kwadratu += 1

        n -= 1
        t.left(90)

rysuj_spirale(18)
turtle.done()