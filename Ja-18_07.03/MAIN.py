"""Zamek szyfrowy"""
# zad.1.
# a)
#   91 -> NIE
#   95 -> TAK
# b)
# 766
# c)
# NIE

# d)
if __name__ == '__main__':
    def znajdz_przedostatnia(n: int) -> int:
        while n > 1:
            r = n % 2
            n = n // 2
        return r

    def zlicz_bity(n: int) -> int:
        l = 0
        while n > 0:
            n = n // 2
            l += 1
        return l

    def sumuj_bity(n: int) -> int:
        s = 0
        while n > 0:
            s += n % 2
            n = n // 2
        return s

    n = int(input())
    przedostatnia = znajdz_przedostatnia(n)
    licz_bity = zlicz_bity(n)
    sumuj_bity = sumuj_bity(n)
    otwiera = False
    print(f'| Przedostatnia: {przedostatnia} |')
    print(f'| Liczba Bitów: {licz_bity} |')
    print(f'| Suma Bitów: {sumuj_bity} |')
    if przedostatnia == 0 and sumuj_bity % 2 == 0 and 2 <= licz_bity <= 10:
        otwiera = True
    print(f'\n\n| Kod zamka      | {n} |')
    print(f'| Otwiera drzwi      | {"Tak" if otwiera else "NIE"} |')