import turtle
import random
from duze_cyfry import daj_cyfre

KOLORY = ['red', 'cyan', 'orange', 'pink', 'magenta', 'green', 'yellow']
bok = 12          # bok jednego kwadracika (w pikselach)
szerokosc = 30    # ile kwadracików w poziomie ma plansza
wysokosc = 30     # ile kwadracików w pionie ma plansza


def pola_cyfry(n, w0, k0):
    """Zwraca listę pól (wiersz, kolumna), które zajmie cyfra n,
    jeśli jej lewy górny róg jest w miejscu (w0, k0)."""
    pola = []
    wiersze = daj_cyfre(n)
    for i in range(5):
        for j in range(5):
            if wiersze[i][j] == '#':
                pola.append((w0 + i, k0 + j))
    return pola


def czy_wolne(pola, plansza):
    """Sprawdza, czy żadne z pól nie jest już zajęte."""
    for pole in pola:
        if pole in plansza:
            return False
    return True


def kolory_sasiadow(pola, plansza):
    """Zwraca listę kolorów kwadracików stykających się z danymi polami."""
    kolory = []
    for (w, k) in pola:
        for sasiad in [(w + 1, k), (w - 1, k), (w, k + 1), (w, k - 1)]:
            if sasiad in plansza:
                kolory.append(plansza[sasiad])
    return kolory


def zrob_mozaike(ile_cyfr):
    """Tworzy mozaikę. Plansza to słownik: (wiersz, kolumna) -> kolor."""
    plansza = {}
    for _ in range(ile_cyfr):
        n = random.randint(0, 9)

        # próbujemy 100 razy znaleźć miejsce dla cyfry
        for _ in range(100):
            w0 = random.randint(0, wysokosc - 5)
            k0 = random.randint(0, szerokosc - 5)
            pola = pola_cyfry(n, w0, k0)

            if not czy_wolne(pola, plansza):
                continue          # kwadraty by na siebie nachodziły

            # wybieramy kolor inny niż kolory sąsiadów
            zle = kolory_sasiadow(pola, plansza)
            dobre = []
            for kolor in KOLORY:
                if kolor not in zle:
                    dobre.append(kolor)
            if len(dobre) == 0:
                continue          # nie ma pasującego koloru

            kolor = random.choice(dobre)
            for pole in pola:
                plansza[pole] = kolor
            break                 # cyfra umieszczona, bierzemy następną
    return plansza

t = turtle.Turtle()
t.hideturtle()
turtle.tracer(0)

def rysuj_kwadrat(x, y, kolor):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(kolor)
    t.begin_fill()
    for _ in range(4):
        t.forward(bok)
        t.right(90)
    t.end_fill()


def rysuj(plansza):
    for (w, k), kolor in plansza.items():
        x = -szerokosc * bok / 2 + k * bok
        y = wysokosc * bok / 2 - w * bok
        rysuj_kwadrat(x, y, kolor)

    turtle.update()
    turtle.done()


rysuj(zrob_mozaike(100))