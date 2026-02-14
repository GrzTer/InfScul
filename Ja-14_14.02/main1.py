""" 2024 - maj NF """

"""Zadanie 1"""
# def wykonaj_nieparzysty_skrot(n: int) -> str | None:
#     b = 1
#     c = 0
#     while n > 0:
#         a = n % 10
#         n //= 10
#         if a % 2 == 0:
#             continue
#         else:
#             c += b * a
#         b *= 10
#     if c == 0: return None
#     return f"--| Nieparzysty skrot wynosi: {c} |--"


# print(wykonaj_nieparzysty_skrot(int(input("Podaj liczbę całkowitą: "))))
"""Zadanie 2"""

# with open('pliki/skrot.txt', 'r') as plik:
#     skroty = [int(i.strip()) for i in plik.readlines()]
# # print(skroty)
#
# n_max_bad = 0
# skroty_bad = []
#
# def wykonaj_nieparzysty_skrot(n: int) -> int | None:
#     b = 1
#     c = 0
#     original_n = n
#     while n > 0:
#         a = n % 10
#         n //= 10
#         if a % 2 == 0:
#             continue
#         else:
#             c += b * a
#             b *= 10
#     if c == 0:
#         return original_n
#     return None


# for n in skroty:
#     wynik = wykonaj_nieparzysty_skrot(n)
#
#     if wynik is not None:
#         if wynik > n_max_bad:
#             n_max_bad = wynik
#         skroty_bad.append(wynik)
#
# print(len(skroty_bad))
# print(n_max_bad)

"""Zadanie 3"""



with open('pliki/skrot2.txt', 'r') as plik:
    skroty = [int(i.strip()) for i in plik.readlines()]
# print(skroty)

def wykonaj_nieparzysty_skrot(n: int) -> int | None:
    b = 1
    c = 0
    original_n = n
    while n > 0:
        a = n % 10
        n //= 10
        if a % 2 == 0:
            continue
        else:
            c += b * a
            b *= 10
    if c == 0:
        return original_n
    return c

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

for n in skroty:
    wynik = wykonaj_nieparzysty_skrot(n)

    if nwd(n, wynik) == 7:
        print(n)