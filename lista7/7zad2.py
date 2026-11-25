from pathlib import Path
import random
import turtle

def obrot_90_prawo(wiersze):
  return [list(wiersz) for wiersz in zip(*reversed(wiersze))]
def rysuj_piksel(x, y, bok, kolor):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pencolor(kolor)
  turtle.fillcolor(kolor)
  turtle.pendown()

  turtle.begin_fill()
  for _ in range(4):
    turtle.forward(bok)
    turtle.left(90)
  turtle.end_fill()


def wczytaj_obraz(sciezka_pliku):
  wiersze = []
  with open(sciezka_pliku, "r", encoding="utf-8") as plik:
    for linia in plik:
      linia = linia.strip()
      if not linia:
        continue
      piksele_w_wierszu = []
      for tekst_piksela in linia.split():
        rgb = eval(tekst_piksela)
        kolor = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
        piksele_w_wierszu.append(kolor)
      wiersze.append(piksele_w_wierszu)
  return wiersze


def obrot_90_prawo(wiersze):
  return [list(wiersz) for wiersz in zip(*reversed(wiersze))]


def obrot_90_lewo(wiersze):
  return [list(wiersz) for wiersz in reversed(list(zip(*wiersze)))]


def rysuj_obraz_losowo(wiersze, bok=10, co_ile=40):
  liczba_wierszy = len(wiersze)
  liczba_kolumn = max((len(w) for w in wiersze), default=0)

  start_x = -(liczba_kolumn * bok) / 2
  start_y = (liczba_wierszy * bok) / 2

  zadania = []
  for indeks_wiersza, wiersz in enumerate(wiersze):
    y = start_y - indeks_wiersza * bok
    for indeks_kolumny, kolor in enumerate(wiersz):
      x = start_x + indeks_kolumny * bok
      zadania.append((x, y, kolor))

  random.shuffle(zadania)

  for licznik, (x, y, kolor) in enumerate(zadania, start=1):
    rysuj_piksel(x, y, bok, kolor)
    if licznik % co_ile == 0:
      turtle.update()

  turtle.update()


def main():
  turtle.tracer(0, 0)
  turtle.colormode(255)
  turtle.speed(0)
  turtle.hideturtle()

  sciezka = Path(__file__).resolve().parent / "niespodzianka.txt"
  obraz = wczytaj_obraz(sciezka)


  obraz = obrot_90_prawo(obraz)
  rysuj_obraz_losowo(obraz, bok=10, co_ile=40)

  turtle.done()


if __name__ == "__main__":
  main()