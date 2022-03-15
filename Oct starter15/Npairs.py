from collections import defaultdict
for _  in range(int(input())):
    N = int(input())
    S = list(map(int, list(input())))
    A1=defaultdict(int)
    A2=defaultdict(int)
    for i in range(N):
        A1[S[i]+i] += 1
        A2[S[i]-i] += 1
    b ,c = 0,0
    for j in A1.values():
        b += (j*(j-1)//2)
    for j in A2.values():
        c += (j*(j-1)//2)
    print(b+c)