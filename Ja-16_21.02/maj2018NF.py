


def zadanie_4_1() -> None:
    wega = [i.strip() for i in open('sygnaly.txt', 'r').readlines()]; przekaz = ""
    for w in range(39,len(wega),40): przekaz += wega[w][9]; print(przekaz)
def zadanie_4_2() -> tuple | None:
    wega = [i.strip() for i in open('sygnaly.txt', 'r').readlines()]
    wega_dict = {}
    for w in wega: wega_dict[w] = len(set(w))
    maximum = max(wega_dict.values())

    for w in wega_dict:
        if wega_dict[w] == maximum: return w, maximum
    return None

def zadanie_4_3() -> None:
    wega = [i.strip() for i in open('sygnaly.txt', 'r').readlines()]
    for w in wega:
        temp_wega = sorted(w)
        if (ord(temp_wega[-1]) - ord(temp_wega[0])) <= 10:
            print("".join(w))

if __name__ == '__main__':
    # print(*zadanie_4_2())
    zadanie_4_3()
