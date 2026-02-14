""" 2025 - majSF - liczba falista"""

"""Zadanie 2"""
def znajdz_liczbe_falista(n: int) -> None:
    b = 1
    c = 0
    a = n % 100
    temp_n = n
    print(a)

    ile = 0
    ile_n = n
    while ile_n > 0:
        ile_n //= 10
        ile += 1

    while temp_n > 0:
        c += b * a
        temp_n //= 100
        b *= 100


    if ile % 2 != 0:
        print((n % 10))
        c //= 10
    print(f"Liczba bazowa : {n} | Liczba falista: {c}")



znajdz_liczbe_falista(int(input("Podaj liczbę całkowitą: ")))

"""Zadanie 1"""
# Liczba bazowa : 78234 | Liczba falista: 34343
# Liczba bazowa : 414141 | Liczba falista: 414141
# Liczba bazowa : 7732 | Liczba falista: 3232
# Liczba bazowa : 21289 | Liczba falista: 89898


