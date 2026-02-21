"""def zadanie1_1() -> None:
    def znajdz_k_podobna(A: list(int), B: list(int)) -> None:
        n = len(A)
        wynik = []

        for k in range(n):
            war1 = (k == 0) or (A[:k] == B[n-k:n])
            war2 = (A[k:] == B[:n-k])

            if war1 and war2:
                wynik.append(k)
        return wynik
    
    # A = [4,7,1,4,5]
    # B = [1,4,5,4,7]
    # A = [1,1,1,1,3,1,1,1,1]
    # B = [3,1,1,1,1,1,1,1,1]
    # A = [1, 2, 3, 4, 5] 
    # B = [3, 4, 5, 1, 2]
    A = [4, 2, 4, 4, 2, 6] 
    B = [4, 4, 2, 6, 4, 2]
    if len(A) == len(B):
        print(*znajdz_k_podobna(A, B))"""
"""def zadanie1_2() -> None:
    def czy_k_podobna(n: int, A: list[int], B: list[int], k: int) -> bool:
        for i in range(k):
            if A[i] != B[n - k + i]:
                return False
        for i in range(k, n):
            if A[i] != B[i - k]:
                return False
        return True

    A = [1, 2, 3, 4, 5]
    B = [3, 4, 5, 1, 2]
    k = 2
    print(f"A={A}\nB={B}\nk={k} -> {czy_k_podobna(len(A), A, B, k)}\n")

    A = [4, 2, 4, 4, 2, 6]
    B = [4, 4, 2, 6, 4, 2]
    k = 1
    print(f"A={A}\nB={B}\nk={k} -> {czy_k_podobna(len(A), A, B, k)}\n")

    A = [5, 7, 9]
    B = [5, 7, 9]
    k = 0
    print(f"A={A}\nB={B}\nk={k} -> {czy_k_podobna(len(A), A, B, k)}")
"""
def zadanie_2() -> None:
    ...

if __name__ == "__main__":
    # zadanie1_1()
    # zadanie1_2()
    zadanie_2()