plik = open('bin.txt', 'r')
wiersze = plik.readlines()


def policz_liczbe_blokow(liczba):
    liczba_blokow = 0
    poprzedni_znak = ''
    for znak in liczba:
        if liczba_blokow == 0:
            liczba_blokow = 1
            poprzedni_znak = znak
        else:
            if znak != poprzedni_znak:
                liczba_blokow = liczba_blokow + 1
                poprzedni_znak = znak
    return liczba_blokow

licznik = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    ile_blokow = policz_liczbe_blokow(wiersz)
    if ile_blokow <= 2:
        licznik += 1
print(licznik)
