def licz_bloki(n) -> None:
    b = 0
    poprzednia = -1
    while n > 0:
        poprzedni = n % 2
        n //= 2
        if poprzedni != poprzednia:
            b += 1
        poprzednia = poprzedni
    return b

"""Zadanie 2.1"""
# if __name__ == "__main__":
#     print(licz_bloki(67))

"""Zadanie 2.2""" # na bin nie na int działać z xor?
if __name__ == "__main__":
    bin = [i.strip() for i in open("bin_przyklad.txt").readlines()]
    print(bin)
    print(*[n for n in bin if licz_bloki(int(n)) <= 2])

"""Zaden 2.4"""
# (123dec XOR 101101bin) XOR 2Dhex = 123dec