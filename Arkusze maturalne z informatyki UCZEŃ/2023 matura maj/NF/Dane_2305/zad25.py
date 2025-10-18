plik = open('bin.txt', 'r')
wiersze = plik.readlines()


for wiersz in wiersze:
    wiersz = wiersz.strip()
    liczba_10 = int(wiersz, 2)
    wynik = liczba_10^(liczba_10 //2)
    print(bin(wynik)[2::])
