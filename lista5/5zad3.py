import random
import turtle
from duze_cyfry import daj_cyfre

def kwadrat(bok, kolor):
    turtle.fillcolor(kolor)
    turtle.pencolor(kolor)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(bok)
        turtle.right(90)
    turtle.end_fill()


def rysuj_cyfre(cyfra, x_start, y_start, rozmiar_kwadratu):
    wzor = daj_cyfre(cyfra)
    kolor = (
        random.random(),
        random.random(),
        random.random(),
    )
    for wiersz_idx, wiersz in enumerate(wzor):
        for kol_idx, znak in enumerate(wiersz):
            if znak == "#":
                x = x_start + kol_idx * rozmiar_kwadratu
                y = y_start - wiersz_idx * rozmiar_kwadratu

                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                kwadrat(rozmiar_kwadratu, kolor)


def rysuj_liczbe(n, rozmiar_kwadratu):
    napis_liczby = str(n)
    liczba_cyfr = len(napis_liczby)

    szerokosc_cyfry = 5 * rozmiar_kwadratu
    odstep = rozmiar_kwadratu
    calkowita_szerokosc = (
        liczba_cyfr * szerokosc_cyfry + (liczba_cyfr - 1) * odstep
    )

    x_aktualny = -calkowita_szerokosc / 2
    y_start = (5 * rozmiar_kwadratu) / 2


    turtle.tracer(0, 0)
    turtle.hideturtle()

    for znak_cyfry in napis_liczby:
        if znak_cyfry.isdigit():
            cyfra = int(znak_cyfry)
        else:
            cyfra = -1

        rysuj_cyfre(cyfra, x_aktualny, y_start, rozmiar_kwadratu)
        x_aktualny += szerokosc_cyfry + odstep

    turtle.update()

rysuj_liczbe(53235523, 25)
turtle.done()