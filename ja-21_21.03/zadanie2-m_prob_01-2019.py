# def zamien_na_dziesietne(x: str, p: int) -> int:
#     w = 0
#     for c in x:
#         if '0' <= c <= '9':
#             w = w * p + ord(c) - ord('0')
#         else:
#             w = w * p + ord(c) - ord('a')
#     return w


def czy_liczba_odkryta(n: int) -> bool:
    m = n
    while n > 0:
        c = n % 10
        n = n // 10
        if c != 0 and m % c != 0:
            return False
    return True


if __name__ == '__main__':
    print(czy_liczba_odkryta(12774))