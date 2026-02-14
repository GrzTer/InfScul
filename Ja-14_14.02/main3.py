""" 2025 - majNF - liczba falista"""


def przestaw(n: int, licznik: int) -> int:
    licznik += 1
    r = n % 100
    a = r // 10
    b = r % 10
    n //= 100
    if n> 0:
        w = a + 10 * b + 100 * przestaw(n, licznik)
    else:
        if a > 0:
            w = a + 10 * b
        else:
            w = b
    print(licznik)
    return w

licznik = 0
# print(przestaw(int(input("Podaj liczbę całkowitą: ")), licznik))
"""Zadanie 1"""
# Liczba : 43657688 | Wywołań: 4
# Liczba : 154005710 | Wywołań: 5
# Liczba : 998877665544321 | Wywołań: 8

"""Zadanie 2"""

# 1 . F
# 2 . P
# 3 . P
# 4 . F

"""Zadanie 3"""
def przestaw(n: int, licznik: int) -> int:
    ...

