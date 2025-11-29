def czy_pierwsza(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
plik = open("5_4.txt", "r")
ile = 0
    for i in range(5000):
        a, b, c = plik.readline().split()
        c = int(c)
        if czy_pierwsza(c) == True:
            ile  += 1
print(ile)

