
def zadanie1_2() -> None:
    def J(n: int) -> None:
        pozycja = 1
        pierwszy = 1
        while n > 0:
            if n % 2 == 1:
                if pierwszy:
                    print(pozycja, end="")
                    pierwszy = 0
                else:
                    print(",", pozycja, end="")
            n //= 2
            pozycja += 1
    n: int = 19; J(19)

def zadanie2_1() -> None:
    licz_wywolania = 0
    def F(x: int, p: int) -> int:
        nonlocal licz_wywolania
        licz_wywolania += 1
        if not x: return 0
        c = x % p
        if c % 2 == 1: return F(x // p, p) + c
        return F(x // p, p) - c
    x, p = map(int, input("Podaj `x` i `p`: ").split())
    wynik = F(x, p)
    print("\n" + "="*60)
    print(f"{'x':>10} | {'p':>10} | {'F(x,p)':>10} | {'Liczba wywołań':>15}")
    print("-"*60)
    print(f"{x:>10} | {p:>10} | {wynik:>10} | {licz_wywolania:>15}")
    print("="*60 + "\n")
def zadanie2_2() -> None:
    def F(x: int, p: int) -> int:
        if not x: return 0
        c = x % p
        if c % 2 == 1: return F(x // p, p) + c
        return F(x // p, p) - c
        
    wyniki = {}

    for p in [3, 4]:
        for x in range(99, 0, -1):
            if F(x, p) == 0:
                wyniki[p] = x
                break

    print("\nZadanie 2.2")
    print("|  p  |  x  |")
    print("|-----|-----|")
    for p in [3, 4]:
        print(f"|  {p}  |  {wyniki[p]} |")


if __name__ == "__main__":
    # zadanie1_2()
    # zadanie2_1()
    zadanie2_2()