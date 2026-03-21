def pisz (s: str,n: int,k: int) -> str:
    # print('*')
    if len(s) == n:
        print(s)
    else:
        for i in range(k):
            pisz(s + str(i), n, k)

if __name__ == '__main__':
    n, k = 3, 2
    pisz('', n, k)