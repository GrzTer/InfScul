# Dodatnią liczbę całkowitą L nazywamy liczbą nieliczną, jeżeli w jej zapisie binarnym cyfry 1 nie sąsiadują ze sobą.

def czy_nieliczna(k: int) -> bool:
    ostatnia = 0
    while k > 0:
        if k % 2 == 1 and ostatnia == 1:
            return False
        ostatnia = k % 2
        k //= 2
    return True


if __name__ == '__main__':
    print(czy_nieliczna(int(input("Jaką liczbę sprawdzamy: "))))