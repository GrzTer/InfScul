J=input()
k=int(input())
W=""

for i in range(k):
    poz=i
    while poz<len(J):
        W += J[poz]
        poz +=k
print(W)
