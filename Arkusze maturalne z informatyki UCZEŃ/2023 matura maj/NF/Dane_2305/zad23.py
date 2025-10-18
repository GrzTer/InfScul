plik = open('bin.txt', 'r')
wiersze = plik.readlines()
najwieksza=0
for wiersz in wiersze:
    liczba_10 = int(wiersz, 2)
    if liczba_10 > najwieksza:
        najwieksza = liczba_10
print(bin(najwieksza)[2::])
