
def zad1(tarcze, strzaly):
    punkty = 0
    for strzal in strzaly:
        for i in range(len(tarcze)):
            if strzal >= tarcze[i][0] and strzal <= (tarcze[i][0] + tarcze[i][1] - 1):
                punkty += 1
                tarcze[i][1] = 0
    return punkty

def zad2(tarcze):
    maks = tarcze[0][1]
    for i in range(len(tarcze)):
        maks = max(maks, tarcze[i][1])

    return maks

def zad3(tarcze):
    maks = 0
    maks_s = 0
    for i in range(1, 5 * 60 + 1):
        punkty = 0
        for tarcza in tarcze:
            if i >= tarcza[0] and i <= (tarcza[0] + tarcza[1] - 1):
                punkty += 1

        if punkty > maks:
            maks = punkty
            maks_s = i

    return maks_s

def zad4(tarcze, strzaly):
    punkty = 0
    for strzal in strzaly:
        for i in range(len(tarcze)):
            if strzal >= tarcze[i][0] and strzal <= (tarcze[i][0] + tarcze[i][1] - 1):
                punkty += 1
    return punkty

dane = open('festyn.txt')
wynik = open('zadanie4.txt', 'w')


for _ in range(3):
    tarcze = []

    n = int(dane.readline())
    for i in range(n):
        a, b = map(int, dane.readline().split(' '))
        tarcze.append([a, b])

    strzaly = []
    m = int(dane.readline())
    for i in range(m):
        t = int(dane.readline())
        strzaly.append(t)

    wynik.write(f'Zadanie 2: {zad2(tarcze)}\n')
    wynik.write(f'Zadanie 3: {zad3(tarcze)}\n')
    wynik.write(f'Zadanie 4: {zad4(tarcze, strzaly)}\n')
    wynik.write(f'Zadanie 1: {zad1(tarcze, strzaly)}\n')
    wynik.write('\n')

dane.close()
wynik.close()