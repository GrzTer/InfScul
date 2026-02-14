""" 2024 - maj NF """

def main(n) -> None:
    b = 1
    c = 0
    licznik = 0
    while n > 0:
        a = n % 10
        n //= 10
        if a % 2 == 0:
            c += b * (a // 2)
        else:
            c += b
            licznik += 1
        b *= 10
    print(f"Liczba c:{c} | licznik:{licznik}")


main(int(input()))


"""Zadanie 1"""
# n: 542102 | Liczba c:121101 | licznik:2
# n: 87654321012345678 | Liczba c:41312111011121314 | licznik:8

"""Zadanie 2"""
# n: 333333666666999999 | Liczba c: 111111333333111111 | licznik: 12