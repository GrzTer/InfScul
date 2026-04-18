# sett: set() = {1,2,3,4,5,6,7,8,9}
# sett2: set() = {1,2,8,9,10,11,12,13}
# print(sett | sett2)
# print(sett ^ sett2)
# print(sett - sett2)
# print(sett & sett2)

def suma(n):
    w = 0
    while n > 0:
        w += n % 10
        n //= 10
    return w


l = [1000, 122, 32, 9]
LL = [[suma(i), i] for i in l]
print(l)
print([i[1] for i in LL])